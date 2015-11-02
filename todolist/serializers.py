from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from todolist.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','status')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password')

    def get_token(self):
        user = User.objects.get(username=self.data['username'])
        return Token.objects.get(user=user).key
