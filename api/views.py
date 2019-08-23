import json
from rest_framework import viewsets, status, views
from .models import Task, TaskExpense
from .serializers import UserSerializer, TaskSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.generics import CreateAPIView
from django.db import transaction
from django.db.transaction import TransactionManagementError
from .validators import user_validate
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()


class ExecutorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(user_type=User.EXECUTOR)
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(user_type=User.CUSTOMER)
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @detail_route(methods=['POST', 'GET'])
    def assign(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, assigned=None)
        except Task.DoesNotExist:
            return Response(json.dumps({"message": "Already taken"}), status=status.HTTP_400_BAD_REQUEST)

        expense, created = TaskExpense.objects.get_or_create(
            task=task,
            executor_id=request.user.pk,
            money=task.money)

        if created:

            with transaction.atomic():
                request.user.update_balance(u"Взял задачу", task.money, task=task)

        Task.objects.filter(pk=pk, assigned=None).update(assigned=request.user)
        return Response(json.dumps({'message': "Taken"}), status=status.HTTP_200_OK)


class RegisterUsersView(CreateAPIView):
    serializer_class=UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user_data = {
            'username' : request.data.get("username"),
            'password' : request.data.get("password"),
            'email' : request.data.get("email"),
            'user_type' : request.data.get("user_type")
        }
        if user_validate(user_data):
            User.objects.create_user(**user_data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(json.dumps({'message': 'User information is not correct'}), status.HTTP_400_BAD_REQUEST)

class UserLoginView(views.APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, **serializer.validated_data)
            if user:
                login(request, user)
                token = jwt_encode_handler(jwt_payload_handler(user))
                return Response({'token': token})
            return Response({'message': 'User unauthorized'},
                            status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'Bad request'},
                        status=status.HTTP_400_BAD_REQUEST)
