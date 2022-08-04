"""
    DAO abstraction level
    Favorite movies DAO class
"""

from .base import BaseDAO
from .models import FavoriteMovies


class FavoriteMovieDAO(BaseDAO[FavoriteMovies]):
    __model__ = FavoriteMovies
    __updatable_fields__ = [
        "user_id",
        "movie_id",
    ]
