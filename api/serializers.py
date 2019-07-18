from rest_framework import serializers
from freelance_arena.users.models import User
from task.models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'first_name', 'last_name', 'username', 'email')


class TaskSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'assignee', 'created_by', 'money')