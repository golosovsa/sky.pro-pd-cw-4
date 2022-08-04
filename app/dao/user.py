"""
    DAO abstraction level
    User DAO class
"""

from .base import BaseDAO
from .models import User


class UserDAO(BaseDAO[User]):
    __model__ = User
    __updatable_fields__ = [
        "email",
        "password",
        "name",
        "surname",
        "favorite_genre_id",
    ]
