from flask_blog import app, db
from flask import render_template, request, session, redirect, url_for
from slugify import slugify
from blog.forms import PostForm
from slugify import slugify
from datetime import datetime
from blog.models import Category, Blog, Post
from author.models import Author
from datetime import datetime

import pdb

POST_PER_PAGE = 5

@app.route('/index/<int:page>', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def  index(page=1):

	posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POST_PER_PAGE, False)

	#print("Total No. of pages: {0}".format(posts.pages))
	#print("Posts per page = %d" % posts.page)

	# for item in posts.items:
	# 	print('Post Title = {0}'.format(item.title))


	# for page in posts.iter_pages():
	# 	if page:
	# 		print(page)
	# 	else:
	# 		print('...')

	print("Post = {0}".format(posts))

	return render_template('blog/index.html', posts = posts)


@app.route('/home', methods = ['GET', 'POST'])
def home():

	posts = Post.query.all()
	return render_template('layout.html', posts = posts)


@app.route('/article/<slug>', methods = ['GET', 'POST'])
def article(slug):

	post = Post.query.filter_by(slug = slug).first()
	author = Author.query.filter_by(id = post.author_id).first()
	category = Category.query.filter_by(id = post.category_id).first()

	return render_template('blog/single_post.html', post = post, author = author.name, category = category.name)




@app.route('/post', methods = ['GET', 'POST'])
def post():

	if session.get('user') is None:
		
		return redirect(url_for('login'))

	form = PostForm()

	if request.method == 'POST':

		if form.validate_on_submit():

			title = form.title.data
			body = form.body.data
			category = form.category.data

			#print("Title = {0}, Body = {1}, Category = {2}".format(title, body, category))

			slug = slugify(title).encode('utf-8')

			author_id = Author.query.filter_by(name = session['user']).first().id
			category_id = Category.query.filter_by(name = str(category)).first().id
			blog_id = Blog.query.first().id

			publish_date = datetime.utcnow()



			#print('Slug = {0},Author ID = {1}, Category = {2}'.format(slug, author_id, category_id))

			post = Post(title, body, slug, blog_id, author_id, category_id, publish_date)
			db.session.add(post)
			db.session.commit()


			return 'Post Added'

	return render_template('author/post.html', form = form)


@app.route('/edit/<int:post_id>', methods = ['GET', 'POST'])
def edit(post_id):

	if session.get('user') is None:
		
		return redirect(url_for('login'))

	
	post_obj = Post.query.filter_by(id = post_id).first_or_404()

	print("POST ID: %d" % post_obj.id)

	form = PostForm(obj = post_obj)

	return render_template('author/post.html', form = form, action = 'update', post = post_obj)


@app.route('/update/<int:post_id>', methods = ['GET', 'POST'])
def update(post_id):

	if session.get('user') is None:
		
		return redirect(url_for('login'))

	form = PostForm()
	post = Post.query.filter_by(id = post_id).first()

	if request.method == 'POST':

			post.title = form.title.data
			post.body = form.body.data 
			post.slug = Post.query.filter_by(id = post_id).first().slug
			post.publish_date = Post.query.filter_by(id = post_id).first().publish_date

			if form.category.data:
				category = Category.query.filter_by(name = str(form.category.data)).first()
				post.category_id = category.id

			print('Category = {0}'.format(category.id))

			blog = Blog.query.first()
			post.blog_id = blog.id

			# author = Author.query.filter_by(username = session['user']).first()
			# post.author_id = author.id


			db.session.commit()

	return redirect(url_for('article', slug = post.slug))


def login_req(f):

	print('login')

	def wrapper_func(*args, **kwargs):

		print('wrapper_func()')

		return f(*args, **args)

	return wrapper_func



@app.route('/delete/<int:post_id>', methods = ['GET', 'POST'])
def delete(post_id):

	if session.get('user') is None:
		
		return redirect(url_for('login'))

	post = Post.query.filter_by(id = post_id).first()

	post.is_live = 0

	db.session.commit()

	return redirect(url_for('index'))





