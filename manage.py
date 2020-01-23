import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_blog import app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand 

from author import views
from blog import views

from author import models
from blog import models

#migrations
migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('runserver', Server(

	use_debugger = True,
	use_reloader = True,
	host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 5000))
	))

manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
	manager.run()