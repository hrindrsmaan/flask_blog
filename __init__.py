from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('settings')

Bootstrap(app)

#database
db = SQLAlchemy(app)



