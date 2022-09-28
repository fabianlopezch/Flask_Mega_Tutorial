# We create the application object "app" as an instance of the class Flask imported from the flask package.
from flask import Flask

app = Flask(__name__)	# app variable inside the app package

from app import routes	# We import the routes module (from app package) at this point because it requires the app variable to be imported