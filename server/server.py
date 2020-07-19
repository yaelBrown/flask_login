from flask import Flask, Blueprint
from flask_cors import CORS

from controllers.UserController import UserController
# from controllers.LoginController import LoginController
# from controllers.RegisterController import RegisterController

import json

app = Flask(__name__)

app.register_blueprint(UserController.users_bp, url_prefix='/api/users')
# app.register_blueprint(LoginController, url_prefix='/api/login')
# app.register_blueprint(RegisterController, url_prefix='/api/register')

@app.route('/')
def hello():
  return {"msg": "Hello!"}, 200

if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')