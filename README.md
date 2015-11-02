# Todolist
Una API para manejar una simple “TODO List”
## Requerimientos
* [Django 1.8](https://www.djangoproject.com/)
* [Django REST Framework 3.1](http://www.django-rest-framework.org/)

## Objetivos
Se implementaron los siguientes endpoints:
* Registrar un usuario.
* Agregar tareas al TODO list.
* Marcar una tarea como resuelta.
* Obtener lista de tareas con su estado actual.
* Autenticaci&oacute;n manejada con [TokenAuthentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

## Instrucciones

Para el correcto funcionamiento se deben instalar los requerimientos anteriores. Se utiliza una base de datos sqlite por defecto.

Ejecutar el servidor de la siguiente forma:

```
python manage.py runserver 0.0.0.0:8000
```
Esto ejecuta el servidor que escucha las peticiones desde cualquier IP, a la IP del servidor ( no sólo localhost ) desde el puerto 8000 por defecto.

# Funciones disponibles

Para realizar las llamadas al servidor se recomienda hacerlas con [Curl](http://curl.haxx.se/) o [Httpie](https://github.com/jkbrzt/httpie)



#pedir token de usuario en particular
 curl -H "Content-Type: application/json" -X POST -d '{"username":<username>, "password":<password>}' http://localhost:8000/todo/get_token/

#pedir lista de tareas
curl -H 'Authorization: Token <token>' -X GET http://localhost:8000/todo/todolist/

