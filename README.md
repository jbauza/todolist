# todolist
lista de tareas por hacer

#pedir token de usuario en particular
 curl -H "Content-Type: application/json" -X POST -d '{"username":<username>, "password":<password>}' http://localhost:8000/todo/get_token/

#pedir lista de tareas
curl -H "Content-Type: aization: Token <token>' -X GET http://localhost:8000/todo/todolist/

