from flask_blog import db

class Register(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(50))
	username = db.Column(db.String(30))
	password = db.Column(db.String(30))
	is_author = db.Column(db.Boolean)

	def __init__(self, name, email, username, password, is_author):
		self.name = name
		self.email = email
		self.username = username
		self.password = password
		self.is_author = is_author

	def __repr__(self):
		return '<Author %r>' % self.username 



class Author(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
	is_author = db.Column(db.Boolean)

	def __init__(self, name, email, username, password):
		self.name = name
		self.email = email
		self.username = username
		self.password = password

	def __repr__(self):
		return "<Author %r>" % self.username
