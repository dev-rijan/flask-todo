from flask_wtf import FlaskForm as Form
from wtforms import HiddenField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Regexp
from wtforms_components import EmailField, Email

from lib.util_wtforms import ModelForm
from todos.blueprints.user.models import User, db
from todos.blueprints.user.validations import ensure_identity_exists, \
    ensure_existing_password_matches, ensure_unique


class LoginForm(Form):
    next = HiddenField()
    identity = StringField('Username or email',
                           [DataRequired(), Length(3, 254)])
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])
    remember = BooleanField('Stay signed in')


class BeginPasswordResetForm(Form):
    identity = StringField('Username or email',
                           [DataRequired(),
                            Length(3, 254),
                            ensure_identity_exists])


class PasswordResetForm(Form):
    reset_token = HiddenField()
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])


class SignupForm(ModelForm):
    email = EmailField(validators=[
        DataRequired(),
        Email(),
        ensure_unique
    ])
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])


class UpdateUsernameForm(ModelForm):
    username_message = 'Letters, numbers and underscores only please.'

    username = StringField(validators=[
        DataRequired(),
        Length(1, 16),
        Regexp('^\w+$', message=username_message),
        ensure_unique
    ])


class UpdateCredentials(ModelForm):
    current_password = PasswordField('Current password',
                                     [DataRequired(),
                                      Length(8, 128),
                                      ensure_existing_password_matches])

    email = EmailField(validators=[
        Email(),
        ensure_unique
    ])
    password = PasswordField('Password', [Optional(), Length(8, 128)])
