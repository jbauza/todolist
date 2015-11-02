# Todolist
Una API para manejar una simple “TODO List”
## Requerimientos
Implementado utilizando:
* [Django 1.8](https://www.djangoproject.com/)
* [Django REST Framework 3.1](http://www.django-rest-framework.org/)

## Objetivos

## Instrucciones

# Funciones disponibles



#pedir token de usuario en particular
 curl -H "Content-Type: application/json" -X POST -d '{"username":<username>, "password":<password>}' http://localhost:8000/todo/get_token/

#pedir lista de tareas
curl -H 'Authorization: Token <token>' -X GET http://localhost:8000/todo/todolist/

