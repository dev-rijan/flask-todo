from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateTimeField, StringField
from wtforms.validators import DataRequired, Length, Optional

from lib.util_wtforms import ModelForm


class SearchForm(FlaskForm):
    q = StringField('Search terms', [Optional(), Length(1, 256)])


class TodoForm(ModelForm):
    description = TextAreaField('Description', validators=[
        DataRequired(),
        Length(1, 8192)
    ])

    todo_at = DateTimeField('Todo at', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
