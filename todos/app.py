from flask import Flask
from werkzeug.debug import DebuggedApplication

from todos.extensions import debug_toolbar
from todos.blueprints.pages import page


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

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)

    return None
