from flask_blog import app, db
from author.forms import RegisterForm, SetupForm, LoginForm
from flask import render_template, request, session
from author.models import Register, Author
from blog.models import Blog, Post
from functools import wraps


POST_PER_PAGE = 5


@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()

	if request.method == 'POST':

		if form.validate_on_submit():

			name = form.name.data
			email = form.email.data
			username = form.username.data
			password = form.password.data

			print("Name = {0}, Email =  {1}, Username = {2}, Password = {3}".format(name, email, username, password))

			#adding data to the database
			try:

				register = Register(name, email, username, password, True)
				db.session.add(register)
				db.session.commit()
				add_flag = True

			except:
				
				add_flag = False
				db.session.rollback()


			if add_flag:
				return 'User Inserted Successfully'
			else: 
				return 'User Adding Failed'
			

	return render_template('author/register.html', form = form)



@app.route('/setup', methods = ['GET', 'POST'])
def setup():
	form = SetupForm()

	if request.method == 'POST':

		if form.validate_on_submit():
			
			blog_name = form.blog_name.data
			author_name = form.author_name.data
			email = form.email.data
			username = form.username.data
			password = form.password.data
			is_author = True

			print("Blog = %s, Author = %s, Email = %s, Username = %s, Password = %s " % (blog_name, author_name, email, username, password))

			author = Author(author_name, email, username, password, is_author)
			db.session.add(author)
			db.session.flush()

			print("Admin ID: %d" % author.id)

			if author.id:
				blog = Blog(blog_name, author.id)
				db.session.add(blog)
				db.session.commit()

			return 'Form Set Up Done!!'

	return render_template('author/setup.html', form = form)




@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()

	if request.method == 'POST':

		if form.validate_on_submit():

			username = form.username.data
			password = form.password.data

			print("Username = {0}, Password = {1}".format(username, password))

			result = Author.query.filter_by(username = username, password = password).first()

			print('Name = {0}, Email = {1}'.format(result.name, result.email))

			if result:
				session['user'] = result.name
				print('Session Started for %s' % session['user'])

				return render_template('author/todo.html')
			else:
				return 'Login Failed!!'

	return render_template('author/login.html', form = form)

	


def login_required(f):
	print(' In login_required() ')

	@wraps(f)
	def decorated_function(*args, **kwargs):
		print('In wrapper_func() ')
		print("User is %s" % session['user'])
		if session.get('username') is None:
			return redirect(url_for('login', next = request.url))
		return f(*args, **kwargs)

	return decorated_function


@login_required
@app.route('/admin')
@app.route('/admin/<int:page>', methods = ['GET', 'POST'])
def admin(page=1):

	posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POST_PER_PAGE, False)


	return render_template('author/admin.html', posts = posts)