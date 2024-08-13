from flask import request
from models.user import UserModel 
from db.user import UserDb

user_db = UserDb("user")

def create_user_services(data: dict):

    user = UserModel(id=None, name=data["name"], last_name=data["last_name"], email=data["email"])

    response = user_db.insert_user(user)

    return response

def users_services():
    return user_db.users()

def user_by_id_service(id: int):

    return user_db.user_by_id(id)

def user_delete_service(id: int):
    
    return user_db.user_delete(id)