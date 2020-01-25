from flask_wtf import Form 
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
	name = StringField('Name', [validators.Required()])
	email = EmailField('Email', [ validators.Required()])
	username = StringField('Username', [ validators.Required(), 
										 validators.Length(min=4, max=20)	
										 ])
	password = PasswordField('Password', [ validators.Required(), 
										   validators.Length(min=5, max=20)])
	confirm = PasswordField('Confirm Password', [ validators.Required(),
												  validators.EqualTo('password')])


class SetupForm(Form):
	blog_name = StringField('Blog Name', [validators.Required()])
	author_name = StringField('Author Name', [validators.Required()])
	email = EmailField('Email', [ validators.Required()])
	username = StringField('Username', [ validators.Required(), 
										 validators.Length(min=4, max=20)	
										 ])
	password = PasswordField('Password', [ validators.Required(), 
										   validators.Length(min=5, max=20)])
	confirm = PasswordField('Confirm Password', [ validators.Required(),
												  validators.EqualTo('password')])



class LoginForm(Form):
	username = StringField("Username", [ validators.Required(), 
										 validators.Length(min = 3, max = 10) ])
	password = StringField("Password", [ validators.Required()])
	
