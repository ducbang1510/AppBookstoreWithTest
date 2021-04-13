from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


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
