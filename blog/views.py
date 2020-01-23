from flask_blog import app

@app.route('/index')
@app.route('/', methods = ['GET', 'POST'])
def  index():
	return 'This will show all the active posts'