from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CustomerForm(FlaskForm):
    first_name = StringField('First_Name', id='billing_first_name', validators=[DataRequired(), Length(min=1, max=100)])
    last_name = StringField('Last_Name', id='billing_last_name', validators=[DataRequired(), Length(min=1, max=100)])
    address = StringField('Address', id='billing_address_1', validators=[DataRequired(), Length(min=1, max=100)])
    email = StringField('Email', id='billing_email', validators=[DataRequired(), Email(), Length(min=6, max=100)])
    phone = StringField('Phone', id='billing_phone', validators=[DataRequired(), Length(min=10, max=10)])
    order_comments = TextAreaField('Order_Comments', id='order_comments')
