""" This file is used to keep the application configuration in a separate file """

import os
basedir = os.path.abspath(os.path.dirname(__file__))	# Provide the directory in which this file is stored

class Config(object):
	""" This class stores configuration variables """

	# Defining the SECRET_KEY configuration varibale. 
	# Flask and some of its extensions use the value of the secret key as a cryptographic
	# 	key, useful to generate signatures or tokens.
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	# Defining database related configuration items 
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')	# The Flask-SQLAlchemy extension takes the location of the application's database from this configuration variable
	SQLALCHEMY_TRACK_MODIFICATIONS = False	# Do not signal the application every time a change is about to be made in the database