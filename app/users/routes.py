from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, login_required, logout_user
from app import create_app, db, login_manager, models
from app.models import User, UserRole
from .forms import RegisterForm, LoginForm
from . import users_blueprint


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # If the User is already logged in, don't allow them to try to register
    if current_user.is_authenticated:
        flash('Đang đăng nhập với tài khoản {}! Vui lòng đăng xuất để sử dụng tài khoản khác'.format(current_user.username))
        return redirect(url_for('store_pages.index'))

    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username_dk.data).first()
        if user:
            flash('Username này đã được sử dụng')
        else:
            new_user = User(name=form.name_dk.data
                            , email=form.email_dk.data
                            , username=form.username_dk.data
                            , password=form.password_dk.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Cảm ơn vì đã đăng kí, {}!'.format(new_user.username))
            return redirect(url_for('store_pages.index'))
    return render_template('users/register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # If the User is already logged in, don't allow them to try to log in again
    if current_user.is_authenticated:
        flash('Đang đăng nhập với tài khoản {}! Vui lòng đăng xuất để sử dụng tài khoản khác'.format(current_user.username))
        return redirect(url_for('store_pages.index'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.is_correct_password(form.password.data):
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)
                flash('Cảm ơn vì đã đăng nhập, {}!'.format(current_user.username))
                if user.user_role == UserRole.ADMIN:
                    return redirect("/admin")
                else:
                    return redirect(url_for('store_pages.index'))

        flash('LỖI! Thông tin đăng nhập không chính xác.')
    return render_template('users/login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Tạm biệt!')
    return redirect(url_for('store_pages.index'))