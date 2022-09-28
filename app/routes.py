""" This module the routes (URLs) that the application implements """

from app import app 

# The @app.route decorator creates an association between the URL given as an argument and the view function (in this case index()).
# View functions are handlers for the application routes.
@app.route('/')
@app.route('/index')
def index():
	return 'Hello, world!'