from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    name_dk = StringField('Name', id='name_dk', validators=[DataRequired(), Length(min=1, max=100)])
    email_dk = EmailField('Email', id='email_dk', validators=[DataRequired(), Email(), Length(min=4, max=100)])
    username_dk = StringField('Username', id='username_dk', validators=[DataRequired(), Length(min=1, max=100)])
    password_dk = PasswordField('Password', id='password_dk', validators=[DataRequired(), Length(min=6, max=30)])
    confirm = PasswordField('Confirm Password', id='password-repeat', validators=[DataRequired(), EqualTo('password_dk')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', id='username', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Password', id='password', validators=[DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
