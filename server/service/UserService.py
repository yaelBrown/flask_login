from .Dbservice import Dbservice
import pymysql

# con = pymysql.Connect(
#   host = Dbservice.DB_HOST, 
#   user = Dbservice.DB_USER, 
#   password = Dbservice.DB_PASSWORD, 
#   database = Dbservice.DB_DATABASE, 
#   charset = Dbservice.DB_CHARSET, 
#   cursorclass = pymysql.cursors.DictCursor, 
#   port = Dbservice.DB_PORT
# )

def __init__(self):
  pass

def getUserByUsername(self, name):
  # search db for username
  return Dbservice.DB_HOST

def registerUser(self, new_user):
  # new_user == dict
  # register new user to database
  pass