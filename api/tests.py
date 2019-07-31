from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
import json
from rest_framework.test import APITestCase, APIClient
from api.models import Task
User = get_user_model()


class ApiUserTests(TestCase):
    client = Client()
    api_url = "/api/v1/"

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user_customer",
            password="qwerty_customer",
            user_type=User.CUSTOMER,
        )
        self.user2 = User.objects.create_user(
            username="user_executor",
            password="qwerty_executor",
            user_type=User.EXECUTOR,
            balance=3000
        )

    def test_registartion_api(self):
        register_url = self.api_url + "register"
        user_data = {
            "username": "gug4thfthurg",
            "email": "mail@mail.ru",
            "password": "passdrword1",
            "user_type" : 1
        }
        response = self.client.post(register_url, user_data)
        self.assertEquals(response.status_code, 201)


    def test_get_list_of_customers(self):
        url = self.api_url + "customers/"
        self.client.login(username="user_customer",password="qwerty_customer")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.data[0].get("username"))
    

    def test_get_list_of_executors(self):
        url = self.api_url + "executors/"
        self.client.login(username="user_customer",password="qwerty_customer")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.data[0].get("username"))

    def test_update_user_information(self):
        url = self.api_url + "customers/"
        self.client.login(username="user_customer",password="qwerty_customer")
        r = self.client.get(url)
        data = {
            "email": "example@example.com"
        }
        user_url = url + str(r.data[0]["id"]) + "/"
        response = self.client.put(user_url, data, content_type='application/json')
        self.assertEquals(response.status_code, 200)

    def test_login_unauthorized(self):
        response = self.client.login(
            username= "some_username",
            password= "some_password"
        )
        self.assertFalse(response)


class ApiTaskTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.api_url = '/api/v1/tasks/'
        self.user = User.objects.create_user(
            username ='user',
            email='user@test.com',
            password='user_password',
            user_type=1,
            balance='100',
        )
        self.user2 = User.objects.create_user(
            username ='user2',
            email='user@test.com',
            password='user2_password',
            user_type=2,
            balance='100',
        )
        self.task = Task.objects.create(
            created_by = self.user,
            description = "setUp task",
            title = "new title",
            money = "500"
        )

    def test_get_task_list(self):
        self.client.login(username='user',password='user_password')
        response = self.client.get(self.api_url)
        self.assertEquals(response.status_code,200)
    
    def test_customer_create_task(self):
        self.client.login(username='user',password='user_password')
        data = {
            'title': 'created_task',
            'description': 'new created task',
            'money': 200
        }
        response = self.client.post(self.api_url, data)
        self.assertEquals(response.status_code,201)

    def test_assign_task(self):
        self.client.login(username='user2', password='user2_password')
        r = self.client.get(api_url)
        assign_url = self.api_url +r[0]['id'] + "/assign" 
        response = self.client.get(assign_url)
        self.assertEquals(response.status_code,200)
        