from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, login_required, logout_user
from app import create_app, db, login_manager, models
from app.models import User
from .forms import RegisterForm, LoginForm
from . import users_blueprint


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # If the User is already logged in, don't allow them to try to register
    if current_user.is_authenticated:
        flash('Already registered!  Redirecting to your User Profile page...')
        return redirect(url_for('store_pages.index'))

    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('This username is duplicate')
        else:
            new_user = User(name=form.name.data
                            , email=form.email.data
                            , username=form.username.data
                            , password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Thanks for registering, {}!'.format(new_user.username))
            return redirect(url_for('store_pages.index'))
    return render_template('users/register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # If the User is already logged in, don't allow them to try to log in again
    if current_user.is_authenticated:
        flash('Already logged in!  Redirecting to your User Profile page...')
        return redirect(url_for('store_pages.index'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.is_correct_password(form.password.data):
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)
                flash('Thanks for logging in, {}!'.format(current_user.username))
                return redirect(url_for('store_pages.index'))

        flash('ERROR! Incorrect login credentials.')
    return render_template('users/login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('store_pages.index'))