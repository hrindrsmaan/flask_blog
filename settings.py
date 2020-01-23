import os

SECRET_KEY = 'abcde'
DEBUG = True

DB_USERNAME = 'flask_blog_user'
DB_PASSWORD = '12345'
DB_HOST = 'localhost'
DB_NAME = 'flask_blog'

DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

