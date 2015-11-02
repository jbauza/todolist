#from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todolist.models import Task
from todolist.serializers import TaskSerializer 

@api_view(['GET','POST'])
#@authentication_classes((SessionAuthentication, TokenAuthentication))
#@permissions_classes((IsAuthenticated,))
def todolist(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def resolve_task(request,name):

    try:
        task = Task.objects.get(name=name)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        if task.status == False:
            task.status = True #estado resuelta
            task.save()
        serializer = TaskSerializer(data={'name':task.name,'status':task.status})
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def task_details(request,pk):

    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TaskSerializer(task,data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
