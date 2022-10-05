# We create the application object "app" as an instance of the class Flask imported from the flask package.
from flask import Flask
from config import Config	# Import the Config class
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)	# Define the variable app inside the app package
app.config.from_object(Config)	# Apply the configurations
db = SQLAlchemy(app)	# Create a database instance
migrate = Migrate(app, db)	# Create a database migration engine instance
login = LoginManager(app) #	Initializing Flask-Login
login.login_view = 'login'

from app import routes, models	# We import the routes module (from app package) at this point because it requires the app variable to be imported
								# Import the module 'models' in which the structure of the database is defined
