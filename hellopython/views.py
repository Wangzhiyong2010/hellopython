from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from hellopython import app, db
from hellopython.models import User

from hellopython.forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()



    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()

        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))

        flash('Invalid username or password.')
        return redirect(url_for('login'))

    return render_template('login.html', form = form)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/kejian')
def kejian():
    return render_template('kejian.html')

@app.route('/guanyu')
def guanyu():
    return render_template('guanyu.html')
