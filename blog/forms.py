from flask_wtf import Form 
from wtforms import StringField, validators, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from blog.models import Category

def categories():
	return Category.query

class PostForm(Form):
	title = StringField('Title', [ validators.Required() ])
	body = TextAreaField('Body', [ validators.Required() ])
	category = QuerySelectField('Category', query_factory = categories, allow_blank = True)


