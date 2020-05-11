from flask_debugtoolbar import DebugToolbarExtension
from flask_static_digest import FlaskStaticDigest
from flask_wtf import CSRFProtect


csrf = CSRFProtect()
debug_toolbar = DebugToolbarExtension()
flask_static_digest = FlaskStaticDigest()