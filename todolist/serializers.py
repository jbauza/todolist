from rest_framework import serializers
from django.contrib.auth.models import User
from todolist.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','status')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id','username')
