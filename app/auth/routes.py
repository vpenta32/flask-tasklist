from flask import render_template, redirect, url_for, flash
from . import auth
from app.forms import *
from app.models import *
from werkzeug.security import generate_password_hash
from .methods import *

from flask_login import login_user, logout_user, login_required, current_user

@auth.route('/')
def index():
    return render_template('auth/auth_main.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        addUser(db, form)
        flash(f'Account created for: {form.username.data}', 'success')
        return redirect(url_for('main.index'))
    if form.password.data != form.confirm_password.data:
        flash('Passwords must match', 'danger')
    return render_template('auth/signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.profile'))
        print("yess")
    else:
        print("none")

    form = LoginForm()
    if form.validate_on_submit():
        user = autenticateUser(db, form)
        if user is not None:
            login_user(user, remember=form.remember_me.data)
            flash(f'Logged in with {form.email.data} account', 'success')
            return redirect(url_for('auth.profile'))
        else:
            flash('Wrong Credentials', 'danger')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth.route('/profile')
@login_required
def profile():
    return render_template('profile/profile.html', user=current_user)