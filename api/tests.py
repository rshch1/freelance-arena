from django.test import TestCase
from django.urls import reverse


class ApiTests(TestCase):

    def test_registartion_api(self):
        user_data = {
            "name": "drgdrrg",
            "username": "gug4thfthurg",
            "email": "mail@mail.ru",
            "password": "passdrword",
            "user_type" : 1
        }
        response = self.client.post(reverse('registration'), user_data)
        self.assertEquals(response.status_code, 201)
