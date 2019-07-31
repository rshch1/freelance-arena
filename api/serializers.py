from rest_framework import serializers
from freelance_arena.users.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'first_name', 'last_name', 'username', 'email')


class TaskSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'assignee', 'created_by', 'money')


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password')
