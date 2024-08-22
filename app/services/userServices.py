from flask import request
from db.user import UserDb
from models.userPayload import UserPayload

user_db = UserDb("user")

def create_user_services(data: dict):

    user = UserPayload(**data)

    response = user_db.insert_user(user)

    return response

def users_services():
    return user_db.users()

def user_by_id_service(id: int):

    return user_db.user_by_id(id)

def user_delete_service(id: int):
    
    return user_db.user_delete(id)

def user_update_service(data: dict):

    print(data)

    user = UserPayload(data["name"], data["last_name"], data["email"])

    response = user_db.user_update(user, data["id"])

    if len(data) == 0:
        return 'invalid pyload', 400
    
    return response
    
