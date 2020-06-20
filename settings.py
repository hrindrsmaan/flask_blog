import os

SECRET_KEY = 'abcde'
DEBUG = True

# DB_USERNAME = 'u8d94mojn94ytjyb'
# DB_PASSWORD = 'G1YmWjlP317GIV8dGM4O'
# DB_HOST = 'btdlgedasioauwrleasy-mysql.services.clever-cloud.com'
# DB_NAME = 'btdlgedasioauwrleasy'

# #DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)

# DB_URI = "mysql+pymysql://u8d94mojn94ytjyb:G1YmWjlP317GIV8dGM4O@btdlgedasioauwrleasy-mysql.services.clever-cloud.com:3306/btdlgedasioauwrleasy"



DB_URI = 'mysql+pymysql://harinder:12345@localhost/flask_blog'


SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
