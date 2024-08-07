from flask import Flask, request
from models.User import User 
from db.Connection import Connection

app = Flask(__name__)

@app.post('/create_user')
def create_user():

    data = request.get_json()

    user = User(id=None, name=data["name"], last_name=data["last_name"], email=data["email"])

    connection = Connection("user")

    response = connection.insert_user(user)

    return response

@app.get('/users')
def users():

    connection = Connection("user")

    response = connection.users()

    print(response)

    return response

if __name__ == '__main__':
    app.run(debug=True)