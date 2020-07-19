from flask import Flask, request, Blueprint, jsonify
from flask_bcrypt import Bcrypt

import service.UserService as UserService
import json

userService = UserService.UserService()

class UserController:
  users_bp = Blueprint('UsersController', __name__)

  @users_bp.route('/login', methods=['POST'])
  def login(self, request):
    user = request.json
    if user != None:
        userCorrect = userService.getUserByUsername(user["username"])
        response = {}
        if userCorrect != None and \
                user["password"] == userCorrect.getPassword() :
            response["result"] = "success"
        else:
            response["result"] = "failed"
        return json.dumps(response)
    else:
        return ""

  def users(self):
      users = userService.allUsers()
      response = []
      for user in users:
          userItem = {}
          userItem["id"] = user.getId()
          userItem["username"] = user.getUsername()
          userItem["password"] = user.getPassword()
          response.append(userItem)
      return json.dumps(response) 