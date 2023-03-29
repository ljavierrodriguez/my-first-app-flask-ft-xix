import json
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/')
def main():
    return jsonify({ "message": "API REST Flask" }), 200

@app.route('/api/users', methods=['GET'])
def get_all_users():
    return jsonify({ "message": "Get all users..."}), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    return jsonify({ "message": "Creating a user..."}), 201

@app.route('/api/users', methods=['PUT'])
def update_user():
    return jsonify({ "message": "Updating a user..."}), 200

@app.route('/api/users', methods=['DELETE'])
def delete_user():
    return jsonify({ "message": "Deleting a user..."}), 200

@app.route('/api/send-info-url/<name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo_by_name(name):
    return jsonify({"message": f"Hola, {name} estas usando el methodo {request.method}"})

@app.route('/api/users/create', methods=['POST'])
def add_user():
    #infor_user = json.loads(request.data)
    #print(infor_user['name'])
    #print(infor_user)

    #info_user = request.get_json()
    #print(info_user['name'])

    name = request.json.get('name')
    phone = request.json.get('phone')

    return jsonify({ "name": name, "phone": phone }), 201

@app.route('/api/users/create', methods=['PUT'])
def edit_user():
    #infor_user = json.loads(request.data)
    #print(infor_user['name'])
    #print(infor_user)

    info_user = request.get_json()
    print(info_user['name'])

    return jsonify(info_user)

if __name__ == '__main__':
    app.run()