import pymysql

class DbService:
  DB_HOST = 'localhost'
  DB_PORT = '3306'
  DB_USER = 'admin'
  DB_PASSWORD = 'admin'
  DB_DATABASE = 'test'
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