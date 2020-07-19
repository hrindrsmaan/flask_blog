from flask_blog import app, db
from flask import render_template, request, session, redirect, url_for, jsonify
from slugify import slugify
from blog.forms import PostForm, ContactUsForm
from slugify import slugify
from datetime import datetime
from blog.models import Category, Blog, Post, ContactUs
from author.models import Author
from datetime import datetime

import pdb

POST_PER_PAGE = 5

@app.route('/index/<int:page>', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def  index(page=1):

	posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POST_PER_PAGE, False)
	categories = Category.query.all()

	return render_template('blog/index.html', posts = posts, categories = categories)


@app.route('/article/<slug>', methods = ['GET', 'POST'])
def article(slug):

	post = Post.query.filter_by(slug = slug).first()
	author = Author.query.filter_by(id = post.author_id).first()
	category = Category.query.filter_by(id = post.category_id).first()

	categories = Category.query.all()

	return render_template('blog/single_post.html', post = post, author = author.name, category = category.name, categories =categories)


@app.route('/post', methods = ['GET', 'POST'])
def post():

	if session.get('user') is None:
		
		return redirect(url_for('login'))

	form = PostForm()

	categories = Category.query.all()

	if request.method == 'POST':

		if form.validate_on_submit():


			if form.category.data:

				category = form.category.data

			elif form.new_category.data:
				
				category = form.new_category.data
				new_category = Category(category)
				db.session.add(new_category)
				db.session.commit()

			else:

				return "Not Category Entered by User !!"

			title = form.title.data
			body = form.body.data
		
			print("Category = {0}".format(category))

			#slug = slugify(title).encode('utf-8')
                        slug = slugify(title)
			author_id = Author.query.filter_by(name = session['user']).first().id
			category_id = Category.query.filter_by(name = str(category)).first().id
			blog_id = Blog.query.first().id
			publish_date = datetime.utcnow()


			print('Slug = {0},Author ID = {1}, Category = {2}'.format(slug, author_id, category_id))

			post = Post(title, body, slug, blog_id, author_id, category_id, publish_date)
			db.session.add(post)
			db.session.commit()


			return 'Post Added'

	return render_template('author/post.html', form = form, categories = categories)


@app.route('/edit/<int:post_id>', methods = ['GET', 'POST'])
def edit(post_id):

	if session.get('user') is None:
		
		return redirect(url_for('login'))

	categories = Category.query.all()
	
	post_obj = Post.query.filter_by(id = post_id).first_or_404()

	print("POST ID: %d" % post_obj.id)

	form = PostForm(obj = post_obj)

	return render_template('author/post.html', form = form, action = 'update', post = post_obj, categories = categories)


@app.route('/update/<int:post_id>', methods = ['GET', 'POST'])
def update(post_id):

	if session.get('user') is None:
		
		return redirect(url_for('login'))



	form = PostForm()
	post = Post.query.filter_by(id = post_id).first()

	categories = Category.query.all()

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


@app.route('/category_wise_blog/<category>')
@app.route('/category_wise_blog/<category>/<int:page>')
def category_wise_blog(category, page=1):

	category = Category.query.filter_by(name = category).first()

	if category:

		#posts = Post.query.filter_by(category_id = category.id).paginate()
		posts = Post.query.filter_by(category_id = category.id).paginate(page, POST_PER_PAGE, False)

		#print("Posts = {0}".format(posts))

		categories = Category.query.all()


	return render_template('blog/category_wise_blog.html', posts = posts,  category = category, categories = categories)


@app.route('/author_wise_posts/<author>')
@app.route('/author_wise_posts/<author>/<int:page>')
def author_wise_posts(author, page = 1):

	categories = Category.query.all()

	if categories:

		author_id = Author.query.filter_by(name = author).first().id

		if author_id:

			posts = Post.query.filter_by(author_id = author_id).paginate(page, per_page = POST_PER_PAGE, error_out = False)

			return render_template('blog/author_wise_posts.html', author = author, posts = posts, categories = categories)

		else:

			return "Something Went Wrong !!"


@app.route('/contact_us', methods = ['GET', 'POST'])
def contact_us():

	form = ContactUsForm()
	categories = Category.query.all()

	if form.validate_on_submit():

		name = form.name.data
		email= form.email.data
		subject = form.subject.data
		message = form.message.data

		contact = ContactUs(name, email, subject, message)

		try:

			db.session.add(contact)
			db.session.commit()

		except Exception as ex:

			db.session.rollback()

		return 'Thanks for contacting us!!'


	return render_template('contact_us.html', form = form, categories = categories )


@app.route('/about', methods = ['GET', 'POST'])
def about():

	categories = Category.query.all()

	return render_template('about.html', categories = categories)





	

	

		


	

	



