from wtforms import TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length

from lib.util_wtforms import ModelForm


class TodoForm(ModelForm):
    description = TextAreaField('Description', validators=[
        DataRequired(),
        Length(1, 8192)
    ])

    todo_at = DateTimeField('Todo at', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
