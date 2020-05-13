from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from flask_wtf import CSRFProtect

csrf = CSRFProtect()
debug_toolbar = DebugToolbarExtension()
flask_static_digest = FlaskStaticDigest()
db = SQLAlchemy()
login_manager = LoginManager()
