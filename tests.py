import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_blog import app, db
from flask import redirect, url_for
import pdb

from flask_blog.author.views import *

from flask_blog.blog.views import *


class UserTest(unittest.TestCase):

    def setUp(self):
        self.db_uri = 'mysql+pymysql://%s:%s@%s/' % ('harinder', '12345', 'localhost')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['BLOG_DATABASE_NAME'] = 'test_blog'
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + app.config['BLOG_DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("create database "  + app.config['BLOG_DATABASE_NAME'])
        db.create_all()
        conn.close()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("drop database "  + app.config['BLOG_DATABASE_NAME'])
        conn.close()


    def create_blog(self):

        return self.app.post('/setup',

        	data = dict(

        	blog_name = 'Test Blog',
        	author_name = 'Harinder',
        	email = 'harinder@gmail.com',
        	username = 'harinder',
        	password = '12345',
        	confirm = '12345'
        	)
        	,

        	follow_redirects = True

        	)

   
   	


    def login(self, username, password):

    	return self.app.post('/login', data = dict(

    		username = username,
    		password = password
    		),

    		follow_redirects = True)

    def login_page_loads(self):

   		return self.app.get('/login')


    def logout(self):

    	return self.app.get('/logout', follow_redirects = True)


    def admin(self):

    	return self.app.get('/admin', follow_redirects = True)


    def index(self):

    	return self.app.get('/', follow_redirects = True)


    def post(self):

    	return self.app.post('/post', 

    		data = dict(

    			title = 'Test Post',
    			body = 'Test Body',
    			category = 'Test category',
    			new_category = 'Test New Category',
    			slug = 'first-post'
    			),

    		follow_redirects = True
    		)


    def update(self):

    	return self.app.post('/update')


    def about(self):

        return self.app.post('/about')


	def test_create_blog(self):

	    	rv = self.create_blog()
	    	assert "User Login" in str(rv.data)


    def test_login_page_loads(self):

    	rv = self.login_page_loads()
    	assert "User Login" in str(rv.data)


    def test_correct_login(self):

    	self.create_blog()
    	rv = self.login('harinder', '12345')
    	assert "Admin Options" in str(rv.data)


    def test_incorrect_login(self):

    	self.create_blog()
    	rv = self.login('wrong', '12345')
    	assert "Login Failed" in str(rv.data)


    def test_logout(self):

    	self.create_blog()
    	self.login('harinder', '12345')
    	rv = self.logout()
    	assert "User Login" in str(rv.data) 


    def test_admin(self):

    	self.create_blog()
    	self.login('harinder', '12345')

    	rv = self.admin()

    	assert "Create" in str(rv.data)


    def test_index(self):

    	self.create_blog()
    	rv = self.index()
    	assert "Read Posts" in str(rv.data)


    def test_about(self):

        rv = self.about()
        assert "Harinder Singh" in str(rv.data)

if __name__ == '__main__':
	unittest.main()


		


