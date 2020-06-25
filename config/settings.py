import os
from dotenv import load_dotenv

# Load env var from dotenv file
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
env_path = os.path.join(APP_ROOT, '.env')
load_dotenv(env_path)

DEBUG = bool(os.getenv('DEBUG', False))

SECRET_KEY = os.getenv('SECRET_KEY', 'secrect_key')
SERVER_NAME = os.getenv('SERVER_NAME', 'localhost:8000')

# AWS
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET = os.getenv('AWS_BUCKET')
AWS_REGION = os.getenv('AWS_REGION')

# SQLAlchemy.
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', '')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SEED_ADMIN_EMAIL = os.getenv('SEED_ADMIN_EMAIL')
SEED_ADMIN_PASSWORD = os.getenv('SEED_ADMIN_PASSWORD')

TIMEZONE = os.getenv('TIMEZONE', 'Asia/Tokyo')
