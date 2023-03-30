import json
import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Todo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db.init_app(app)
# flask db init, flask db migrate, flask db upgrade, flask db downgrade
Migrate(app, db)
""" 
ACTIVAR COMANDO: flask
windows: SET FLASK_APP=src/app.py
Mac o Linux: export FLASK_APP=src/app.py
"""
CORS(app)


@app.route('/')
def main():
    return jsonify({"message": "API REST Flask"}), 200


@app.route('/apis/fake/todos/user/<username>', methods=['GET'])
def get_todo_list(username):

    todo = Todo.query.filter_by(username=username).first()  # <Todo lrodriguez>

    if not todo:
        return jsonify({"msg": "Please use POST method to create a user."}), 404

    # { "tasks": '[{'label': 'Sample Task', 'done': False}]' }
    todo = todo.serialize()
    # [{'label': 'Sample Task', 'done': False}]
    datos = json.loads(todo['tasks'])

    return jsonify(datos), 200


@app.route('/apis/fake/todos/user/<username>', methods=['POST'])
def create_todo_list(username):

    body = request.get_json()

    if len(body) > 0:
        return jsonify({"msg": "Body must be an empty array..."}), 400

    body.append({"label": "Sample Task", "done": False})

    todo = Todo.query.filter_by(username=username).first()

    if todo: return jsonify({"msg": "Please use GET method to get todo list by user."}), 400

    todo = Todo()
    todo.username = username
    todo.tasks = json.dumps(body)
    todo.save()

    if todo:
        return jsonify({
            "result": "ok"
        }), 201
    else:
        return jsonify({
            "result": "fail"
        }), 400


@app.route('/apis/fake/todos/user/<username>', methods=['PUT'])
def update_todo_list(username):

    body = request.get_json()

    if len(body) == 0:
        return jsonify({"msg": "Body must be an array with tasks..."}), 400

    total = len(body)

    todo = Todo.query.filter_by(username=username).first()

    if not todo:
        return jsonify({"msg": "Please use POST method to create a user."}), 404

    todo.tasks = json.dumps(body)
    todo.update()

    if todo:
        return jsonify({
            "result": f"A list with {total} todos was succesfully saved"
        }), 200
    else:
        return jsonify({
            "result": "fail"
        }), 400


@app.route('/apis/fake/todos/user/<username>', methods=['DELETE'])
def delete_todo_list(username):

    todo = Todo.query.filter_by(username=username).first()

    if not todo:
        return jsonify({"msg": "Please use POST method to create a user."}), 404

    todo.delete()

    return jsonify({"result": "ok"}), 200

# Usar si usamos por defecto SQLIte
# with app.app_context():
#    db.create_all()


if __name__ == '__main__':
    app.run()
