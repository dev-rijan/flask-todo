from wtforms.validators import ValidationError

from todos.blueprints.user.models import User


def ensure_identity_exists(form, field):
    """
    Ensure an identity exists.

    :param form: wtforms Instance
    :param field: Field being passed in
    :return: None
    """
    user = User.find_by_identity(field.data)

    if not user:
        raise ValidationError('Unable to locate account.')


def ensure_existing_password_matches(form, field):
    """
    Ensure that the current password matches their existing password.

    :param form: wtforms Instance
    :param field: Field being passed in
    :return: None
    """
    user = User.query.get(form._obj.id)

    if not user.authenticated(password=field.data):
        raise ValidationError('Does not match.')


def ensure_unique(form, field):
    """
    Ensure that given field is unique


    :param form: wtforms Instance
    :param field: Field being passed in
    :return: None
    """

    db_field = field.name

    query = {db_field: field.data}

    user = User.query.filter_by(**query).first()

    if not user:
        return True

    if not form._obj or user.id != form._obj.id:
        raise ValidationError(f'{db_field.capitalize()} must be unique')
