import os

SECRET_KEY = 'abcde'
DEBUG = True

DB_USERNAME = 'flask_blog_user'
DB_PASSWORD = '12345'
DB_HOST = 'localhost'
DB_NAME = 'flask_blog'

#DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)

DB_URI = "mysql+pymysql://u8d94mojn94ytjyb:G1YmWjlP317GIV8dGM4O@btdlgedasioauwrleasy-mysql.services.clever-cloud.com:3306/btdlgedasioauwrleasy"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
