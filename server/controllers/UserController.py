from flask import Flask, request, Blueprint, jsonify
from flask_bcrypt import Bcrypt

import service.UserService as UserService
import json

UserController = Blueprint('UsersController', __name__)

@UserController.route('/login', methods=['POST'])
def login():
  user = request.json

  if user != None:
    try: 
      db_user = UserService.getUserByUsername(user.get("username"))
      
      if Bcrypt.check_password_hash(db_user["password"], user["password"]):
        
        out = {
          "username": db_user["username"],
          "email": db_user["email"],
          "group": db_user["group"]
        }
        
        return { "msg": "Successful login", "data": out }, 200
      
      else:
        return { "msg": "Unsuccessful login"}
    
    except Exception as e:
      return { "msg": f"Error trying to authenticate user {user['username']}", "Error": e }, 422

@UserController.route('/register', methods=['POST'])
def register(request):
  user = request.json
  
  if user != None: 
    try:

      newUser = {
        "username": user["username"],
        "password": Bcrypt.generate_password_hash(user["password"], rounds=12),
        "email": user["email"],
        "group": user["group"],
        "2fa": False
      }
      
      userService.registerUser(newUser)
      
      del newUser["password"]
      
      return { "msg": "Successfully register user", "data": newUser }, 200
    
    except Exception as e:
      return { "msg": f"Error trying to register user: {user['username']}", "error": e }, 422
