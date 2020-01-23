from flask_blog import app, db
from author.forms import RegisterForm
from flask import render_template, request
from author.models import Register 

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


@app.route('/login', methods = ['GET', 'POST'])
def login():
	return 'Login'