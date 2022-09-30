""" This file is used to keep the application configuration in a separate file """

import os

class Config(object):
	""" This class stores configuration variables """

	# Defining the SECRET_KEY configuration varibale. 
	# Flask and some of its extensions use the value of the secret key as a cryptographic
	# 	key, useful to generate signatures or tokens.
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'