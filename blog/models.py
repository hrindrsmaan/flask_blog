from flask_blog import db

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))
	admin = db.Column(db.Integer, db.ForeignKey("author.id"))

	def __init__(self, name, admin):
		self.name = name
		self.admin = admin


	def __repr__(self):
		return "<Blog %r>" %self.name



class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(255))
	body = db.Column(db.String(1000))
	slug = db.Column(db.String(255))

	publish_date = db.Column(db.Date)
	blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))
	author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
	category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

	def __init__(self, title, body, slug, blog_id, author_id, category_id, date):
		self.title = title
		self.body = body
		self.slug = slug
		self.blog_id = blog_id
		self.author_id = author_id
		self.category_id = category_id
		self.publish_date = date

	def __repr__(self):
		return "<Post %r>" % self.title
