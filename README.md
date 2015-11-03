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
* Autenticacion manejada con [TokenAuthentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

## Instrucciones

Para el correcto funcionamiento se deben instalar los requerimientos anteriores. Se utiliza una base de datos sqlite por defecto.

Ejecutar el servidor de la siguiente forma:

```
python manage.py runserver 0.0.0.0:8000
```
Esto ejecuta el servidor que escucha las peticiones desde cualquier IP, a la IP del servidor ( no sólo localhost ) desde el puerto 8000 por defecto.

# Funciones disponibles

Para realizar las llamadas al servidor se recomienda hacerlas con [Curl](http://curl.haxx.se/) o [Httpie](https://github.com/jkbrzt/httpie)

## Registrar usuario

Registra un nuevo usuario y retorna el token generado, que servira para realizar todas las transacciones posteriores. No necesita autorizacion y se debe enviar *username* y *password*

### Input
```
curl -H "Content-Type: application/json" -X POST -d '{"username":"<username>", "password":"<password>"}' http://localhost:8000/todo/register_user/
```
### Output
```
{"<token>"}
```

## Pedir token de usuario

Pide un token de un usuario ya registrado. No necesita autorizaci&oacute;n y se debe enviar *username* y *password*
### Input
```
curl -H "Content-Type: application/json" -X POST -d '{"username":"<username>", "password":"<password>"}' http://localhost:8000/todo/get_token/
```
### Output
```
{"token":"<token>"}
```

## Pedir lista de tareas

Pide todas las tareas disponibles con sus estados correspondientes se debe enviar el *token* en el header, para pasar la autorizacion.

### Input
```
curl -H 'Authorization: Token <token>' -X GET http://localhost:8000/todo/todolist/
```
### Output
```
 [
 {"name":"tareita","status":false},
 {"name":"tarea2","status":true"},
 {"name":"nueva_tarea","status":true}
 ]
```

## Agregar tarea
Agrega una nueva tarea a la todolist. Se debe enviar token en header y el *name* de la nueva tarea vía POST
### Input
```
curl -H "Content-Type: application/json" -H 'Authorization: Token <token>' -X POST -d '{"name":"<task_name>"}' http://localhost:8000/todo/add_task/
```
### Output
```
{"name":"tareita","status":false}
```

## Resolver Tarea
Resuelve una tarea y le cambia el status de *false* a *true*. Se debe enviar el *task_name* al final de la url vía POST
### Input
```
curl -H "Content-Type: application/json" -H 'Authorization: Token <token>' -X POST http://localhost:8000/todo/resolve_task/<task_name>
```
### Output
```
{"name":"tareita","status":true}
```

