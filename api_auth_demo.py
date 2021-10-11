import hashlib
import secrets

from flask import Flask
from flask_restful import abort, Api, Resource, request

app = Flask(__name__)
api = Api(app)

users = [
    {'username': 'john', 'hash': '0231a657082c47e0a1d2b42736023adb1248c9307dcd3a55ee28bb2f0ea22926aa8110567130750c0fe95a86a2553c65c05b9c8ee2e1694f83fe9867f7696a3b', 'token': ''} #password: hello
]


class User(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')

        if username is None or password is None:
            abort(400, message="Username/Password not provided")

        user_exists = any(username in user['username'] for user in users)
        if user_exists:
            abort(400, message="Username in use")

        salt = '5AlT!'
        lib = hashlib.sha512()
        lib.update(salt.encode('utf-8'))
        lib.update(password.encode('utf-8'))
        user_hash = lib.hexdigest()
        user_token = secrets.token_urlsafe()
        user = {'username': username, 'hash': user_hash, 'token': user_token}
        users.append(user)

        responseObject = {
            'message': 'User successfully registered',
            'auth_token': user_token
        }
        return responseObject, 201


api.add_resource(User, '/api/user')


@app.route("/api/login", methods=['POST'])
def user_login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = next((item for item in users if item['username'] == username), None)
    if user is None:
        abort(400, message="Username not registered. Please create an account.")

    salt = '5AlT!'
    lib = hashlib.sha512()
    lib.update(salt.encode('utf-8'))
    lib.update(password.encode('utf-8'))
    user_hash = lib.hexdigest()
    if user_hash != user['hash']:
        abort(400, message="Incorrect password.")

    user_token = secrets.token_urlsafe()

    for i in range(len(users)):
        if users[i]['username'] == username:
            users[i]['token'] = user_token

            responseObject = {
                'message': 'Login successful',
                'auth_token': user_token
            }
            return responseObject, 201


@app.route("/api/doSomething", methods=['GET'])
def user_something():
    if 'token' not in request.headers:
        abort(400, message="Token not provided")

    token = request.headers['token']
    user_exists = any(token in user['token'] for user in users)
    if user_exists is False:
        abort(400, message="Invalid token not provided")
    else:
        responseObject = {
            'message': 'You are an authenticated user. Here is the data...'
        }
        return responseObject, 201


@app.route("/api/logout", methods=['POST'])
def user_logout():
    if 'token' not in request.headers:
        abort(400, message="Token not provided")

    token = request.headers['token']
    for i in range(len(users)):
        if users[i]['token'] == token:
            users[i]['token'] = ''

            responseObject = {
                'message': 'User successfully logged out'
            }
            return responseObject, 201

    abort(400, message="Invalid token")


if __name__ == '__main__':
    app.run(debug=True)
