from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings.config import MIGRATION_DIR

db = SQLAlchemy()
migrate = Migrate(db=db, directory=MIGRATION_DIR)
