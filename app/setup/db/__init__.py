from flask_sqlalchemy import SQLAlchemy
from .models import Base, BaseWithID, BaseManyToMany

db = SQLAlchemy()

__all__ = [
    "db",
    "Base",
    "BaseWithID",
    "BaseManyToMany",
]
