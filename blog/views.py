from flask_blog import app, db
from flask import render_template, request, session, redirect
from slugify import slugify
from blog.forms import PostForm
from slugify import slugify
from datetime import datetime
from blog.models import Category, Blog, Post
from author.models import Author
from datetime import datetime



@app.route('/index', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def  index():

	posts = Post.query.all()

	for post in posts:
		print("Title %s" % post.title)


	return render_template('blog/index.html', posts = posts)



@app.route('/article/<slug>', methods = ['GET', 'POST'])
def article(slug):

	post = Post.query.filter_by(slug = slug).first()

	return render_template('blog/single_post.html', post = post)


@app.route('/post', methods = ['GET', 'POST'])
def post():
	form = PostForm()

	if request.method == 'POST':

		if form.validate_on_submit():

			title = form.title.data
			body = form.body.data
			category = form.category.data

			print("Title = {0}, Body = {1}, Category = {2}".format(title, body, category))

			slug = slugify(title).encode('utf-8')

			author_id = Author.query.filter_by(name = session['user']).first().id
			category_id = Category.query.filter_by(name = str(category)).first().id
			blog_id = Blog.query.first().id

			publish_date = datetime.utcnow()



			print('Slug = {0},Author ID = {1}, Category = {2}'.format(slug, author_id, category_id))

			post = Post(title, body, slug, blog_id, author_id, category_id, publish_date)
			db.session.add(post)
			db.session.commit()


			return 'Post Added'

	return render_template('author/post.html', form = form)



@app.route('/admin', methods = ['GET', 'POST'])
def admin():

	posts = Post.query.order_by(Post.publish_date.desc())

	return render_template('author/admin.html', posts = posts)