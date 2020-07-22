import pymysql

class DbService:
  DB_HOST = ''
  DB_PORT = ''
  DB_USER = ''
  DB_PASSWORD = ''
  DB_DATABASE = ''
  DB_CHARSET = ''

  con = pymysql.Connect(
    host = DB_HOST, 
    user = DB_USER, 
    password = DB_PASSWORD, 
    db = DB_DATABASE, 
    charset = DB_CHARSET, 
    cursorclass = pymysql.cursors.DictCursor, 
    port = DB_PORT
  )