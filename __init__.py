from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object('settings')

#database
db = SQLAlchemy(app)



