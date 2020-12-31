import os

SECRET_KEY = 'abcde'
DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = 'test'
DB_HOST = 'mysql:3306'
DB_NAME = 'blog'

#DEVELOPMENT MYSQL URI
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)

#PRODUCTION MYSQL URI
#DB_URI = "mysql+pymysql://u8d94mojn94ytjyb:G1YmWjlP317GIV8dGM4O@btdlgedasioauwrleasy-mysql.services.clever-cloud.com:3306/btdlgedasioauwrleasy"

#DB_URI = 'mysql+pymysql://harinder:12345@localhost/flask_blog'
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True
