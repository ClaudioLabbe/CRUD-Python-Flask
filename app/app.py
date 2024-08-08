from flask import Flask
from routes.todo import todo

app = Flask(__name__)

app.register_blueprint(todo, url_prefix='/app')

if __name__ == '__main__':
    app.run(debug=True)