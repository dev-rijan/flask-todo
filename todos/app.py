from flask import Flask
from werkzeug.debug import DebuggedApplication
from cli import register_cli_commands
from todos.blueprints.user import user
from itsdangerous import URLSafeTimedSerializer

from todos.blueprints.user.models import User
from todos.extensions import csrf, debug_toolbar, flask_static_digest, db, login_manager
from todos.blueprints.pages import page
from todos.blueprints.user import user


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, static_folder='../public', static_url_path='')

    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)

    extensions(app)

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    app.register_blueprint(page)
    app.register_blueprint(user)
    register_cli_commands(app)

    authentication(app, User)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    csrf.init_app(app)
    debug_toolbar.init_app(app)
    db.init_app(app)
    flask_static_digest.init_app(app)
    login_manager.init_app(app)

    return None


def authentication(app, user_model):
    """
    Initialize the Flask-Login extension (mutates the app passed in).

    :param app: Flask application instance
    :param user_model: Model that contains the authentication information
    :type user_model: SQLAlchemy model
    :return: None
    """
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)

    # @login_manager.token_loader
    # def load_token(token):
    #     duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
    #     serializer = URLSafeTimedSerializer(app.secret_key)
    #
    #     data = serializer.loads(token, max_age=duration)
    #     user_uid = data[0]
    #
    #     return user_model.query.get(user_uid)
