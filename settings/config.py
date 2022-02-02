import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get("DEBUG", True)
TESTING = os.environ.get("DEBUG", True)

# Database settings
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
                          "sqlite:///" + os.path.join(BASE_DIR, "app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = True
MIGRATION_DIR = os.environ.get('MIGRATION_DIR', os.path.join(BASE_DIR, "models", "migrations"))