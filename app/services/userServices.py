from flask import request
from models.user import UserModel 
from db.user import UserDb

def create_user_services():

    data = request.get_json()

    user = UserModel(id=None, name=data["name"], last_name=data["last_name"], email=data["email"])

    user_db = UserDb("user")

    response = user_db.insert_user(user)

    return response

def users_services():

    user_db = UserDb("user")

    response = user_db.users()

    return response