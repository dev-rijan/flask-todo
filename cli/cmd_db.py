import click
from flask import current_app
from flask.cli import with_appcontext

from sqlalchemy_utils import database_exists, create_database

from todos.extensions import db as database
from todos.blueprints.user.models import User


@click.group()
@with_appcontext
def db():
    """ Run PostgreSQL related tasks. """
    pass


@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False,
              help='Create a test db too?')
@with_appcontext
def init(with_testdb):
    """
    Initialize the database.

    :param with_testdb: Create a test database
    :return: None
    """
    database.drop_all()
    database.create_all()

    if with_testdb:
        db_uri = '{0}_test'.format(current_app.config['SQLALCHEMY_DATABASE_URI'])

        if not database_exists(db_uri):
            create_database(db_uri)

    return None


@click.command()
@with_appcontext
def seed():
    """
    Seed the database with an initial user.

    :return: User instance
    """
    if User.find_by_identity(current_app.config['SEED_ADMIN_EMAIL']) is not None:
        return None

    params = {
        'role': 'admin',
        'email': current_app.config['SEED_ADMIN_EMAIL'],
        'password': current_app.config['SEED_ADMIN_PASSWORD']
    }

    return User(**params).save()


@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False,
              help='Create a test db too?')
@click.pass_context
def reset(ctx, with_testdb):
    """
    Init and seed automatically.

    :param with_testdb: Create a test database
    :return: None
    """
    ctx.invoke(init, with_testdb=with_testdb)
    ctx.invoke(seed)

    return None


db.add_command(init)
db.add_command(seed)
db.add_command(reset)
