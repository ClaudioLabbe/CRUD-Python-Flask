from flask import Blueprint, request
from services.userServices import users_services, create_user_services, user_by_id_service, user_delete_service, user_update_service

todo = Blueprint('todo', __name__)

@todo.post('/create_user')
def create_user():
    data = request.get_json()

    return create_user_services(data)

@todo.get('/users')
def users():

    return users_services()

@todo.get('/user_by_id')
def user_by_id():
    return user_by_id_service(request.args.get('id'))

@todo.delete('/user_delete/<int:id>')
def user_delete(id):
    return user_delete_service(id)

@todo.put('/user_update')
def user_update():
    data = request.get_json()

    return user_update_service(data)