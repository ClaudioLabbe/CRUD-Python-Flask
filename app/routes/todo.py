from flask import Blueprint
from services.userServices import users_services, create_user_services

todo = Blueprint('todo', __name__)

@todo.post('/create_user')
def create_user():

    return create_user_services()

@todo.get('/users')
def users():

    return users_services()