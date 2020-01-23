from flask_blog import db

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))
	admin = db.Column(db.Integer, db.ForeignKey("author.id"))

	def __init__(self):
		self.name = name

	def __repr__(self):
		return "<Blog %r>" %self.name