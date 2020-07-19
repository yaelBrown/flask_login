from flask import Flask, Blueprint
from flask_cors import CORS

from controllers.UserController import UserController

import json

app = Flask(__name__)

app.register_blueprint(UserController.UserController, url_prefix='/api/users')

@app.route('/')
def hello():
  return {"msg": "Hello!"}, 200

if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')