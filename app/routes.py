""" This module handles the routes (URLs) that the application implements """

from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User 
from flask_login import logout_user
from flask_login import login_required

# The @app.route decorator creates an association between the URL given as an argument and the view function (in this case index()).
# View functions are handlers for the application routes.
@app.route('/')
@app.route('/index')
@login_required
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

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	# Receiving login credentials
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
