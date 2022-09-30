# We create the application object "app" as an instance of the class Flask imported from the flask package.
from flask import Flask
from config import Config	# Import the Config class

app = Flask(__name__)	# Define the variable app inside the app package
app.config.from_object(Config)	# Apply the configurations

from app import routes	# We import the routes module (from app package) at this point because it requires the app variable to be imported