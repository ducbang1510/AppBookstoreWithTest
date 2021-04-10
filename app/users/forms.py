from app import admin, db
from app.models import *
from flask import redirect
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class MyView(BaseView):
    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(MyView, self).__init__(*args, **kwargs)
        self.admin = admin


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyModelView(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_export = True
    can_delete = True


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('users/contact.html')


class LogOutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(LogOutView(name="Đăng xuất"))
admin.add_view(ContactView(name='Liên hệ'))
admin.add_view(MyModelView(User, db.session, name='Khách hàng'))


class RegisterForm(FlaskForm):
    name = StringField('Name', id='name_dk', validators=[DataRequired(), Length(min=1, max=100)])
    email = StringField('Email', id='email_dk', validators=[DataRequired(), Email(), Length(min=6, max=100)])
    username = StringField('Username', id='username_dk', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Password', id='password_dk', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Confirm Password', id='password-repeat', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', id='username', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Password', id='password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
