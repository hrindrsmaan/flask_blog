from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_bootstrap import Bootstrap


app = Flask(__name__)
#app.config.from_object('settings')
app.config['SECRET_KEY'] = 'abcde'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://u8d94mojn94ytjyb:G1YmWjlP317GIV8dGM4O@btdlgedasioauwrleasy-mysql.services.clever-cloud.com:3306/btdlgedasioauwrleasy'

Bootstrap(app)

#database
db = SQLAlchemy(app)



