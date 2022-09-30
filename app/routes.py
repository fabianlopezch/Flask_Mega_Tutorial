""" This module handles the routes (URLs) that the application implements """

from flask import render_template
from app import app 
from app.forms import LoginForm

# The @app.route decorator creates an association between the URL given as an argument and the view function (in this case index()).
# View functions are handlers for the application routes.
@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'Carlos'}
	posts = [
			{
				'author' : {'username' : 'John'},
				'body' : 'Beautiful day in portland!',
			},
			{
				'author' : {'username' : 'Susan'},
				'body' : 'The avengers movie was so cool!',
			}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
	form = LoginForm()
	# Receiving login credentials
	if form.validate_on_submit():
		flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)

