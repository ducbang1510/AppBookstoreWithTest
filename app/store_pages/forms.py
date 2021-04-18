from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    kw = StringField('Search', validators=[Length(min=1, max=100)])
    # submit = SubmitField('Login')
