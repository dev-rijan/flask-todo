from collections import OrderedDict

from flask_wtf import Form
from wtforms import SelectField, StringField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from lib.util_wtforms import ModelForm, choices_from_dict
from todos.blueprints.user.models import db, User


class SearchForm(Form):
    q = StringField('Search terms', [Optional(), Length(1, 256)])


class BulkDeleteForm(Form):
    SCOPE = OrderedDict([
        ('all_selected_items', 'All selected items'),
        ('all_search_results', 'All search results')
    ])

    scope = SelectField('Privileges', [DataRequired()],
                        choices=choices_from_dict(SCOPE, prepend_blank=False))


class UserForm(ModelForm):
    username_message = 'Letters, numbers and underscores only please.'

    username = StringField(validators=[
        Optional(),
        Length(1, 16),
        Regexp('^\w+$', message=username_message)
    ])

    role = SelectField('Privileges', [DataRequired()],
                       choices=choices_from_dict(User.ROLE,
                                                 prepend_blank=False))
    active = BooleanField('Yes, allow this user to sign in')
