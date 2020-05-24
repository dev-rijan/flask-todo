import os
from dotenv import load_dotenv

# Load env var from dotenv file
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
env_path = os.path.join(APP_ROOT, '.env')
load_dotenv(env_path)

DEBUG = True

SECRET_KEY = os.getenv('SECRET_KEY', 'secrect_key')
SERVER_NAME = 'localhost:8000'

# SQLAlchemy.
db_uri = 'postgresql://admin:admin@localhost:5432/todos'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

SEED_ADMIN_EMAIL = "rijan@test.test"
SEED_ADMIN_PASSWORD = "admin45678"
