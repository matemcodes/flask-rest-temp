from utils.close import exit_app

try:
    from sqlalchemy import exc
    from flask_sqlalchemy import SQLAlchemy
except ImportError as ex: exit_app(f"Module not found: {ex}")

try: db = SQLAlchemy()
except exc.SQLAlchemyError as ex:
    exit_app(f"Failed to create db: {ex}")