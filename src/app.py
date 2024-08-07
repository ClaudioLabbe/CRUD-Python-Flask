from flask import Flask, jsonify
from models.User import User
from dataclasses import asdict

app = Flask(__name__)

@app.get('/searchAll')
def searchAll():

    user = User(name='Claudio', email='c.labbe.tudela@gmail.com', lastName='Labbe')

    return jsonify(asdict(user))

if __name__ == '__main__':
    app.run(debug=True)