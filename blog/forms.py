from flask_wtf import Form 
from wtforms import StringField, validators, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from blog.models import Category
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField

def categories():
	return Category.query

class PostForm(Form):
	title = StringField('Title', [ validators.Required() ])
	#body = TextAreaField('Body', [ validators.Required() ])
	body = StringField('Body', widget=TextArea())
	category = QuerySelectField('Category', query_factory = categories, allow_blank = True)
	new_category = StringField('New Category')


class ContactUsForm(Form):

	name = StringField('Name', [ validators.Required()])
	email = EmailField('Email', [ validators.Required() ])
	subject = StringField('Subject', [ validators.Required()])
	message = StringField('Message', [ validators.Required() ] ,widget=TextArea())
	

