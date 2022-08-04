"""
    DAO abstraction level
    Movie DAO class
"""

from .base import BaseDAO
from .models import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie
    __updatable_fields__ = [
        "title",
        "description",
        "trailer",
        "year",
        "rating",
        "genre_id",
        "director_id",
    ]
