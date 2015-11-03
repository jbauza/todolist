from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from django.contrib.auth.models import User
from todolist.models import Task

class User_Registration(APITestCase):

    def test_user_registration(self):

        url = reverse('register_user')
        data = {'username':'test','password':'test'}
        response = self.client.post(url,data,format='json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.get().username, 'test')
        

class Task_Test(APITestCase):


    def test_add_task(self):
        url = reverse('add_task')
        data = {'name':'test_task'}
        user = User.objects.create(username='test')
        self.client.force_authenticate(user=user)
        response = self.client.post(url,data,format='json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(),1)
        self.assertEqual(Task.objects.get().name, 'test_task')
        
    def test_todolist(self):
        url = reverse('todolist')
        user = User.objects.create(username='test')
        self.client.force_authenticate(user=user)
        response = self.client.get(url)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_resolve_task(self):
        task_name = 'test_task'
        url = '/todo/resolve_task/'+task_name
        user = User.objects.create(username='test')
        task = Task.objects.create(name=task_name)

        self.assertEqual(task.status, False)

        self.client.force_authenticate(user=user)
        response = self.client.post(url)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().status, True)
        
