"""
    Service abstraction level
    Movie service class
"""

from .base import BaseService
from app.dao import FavoriteMovieDAO


class FavoriteMovieService(BaseService[FavoriteMovieDAO]):
    def __init__(self, dao: FavoriteMovieDAO):
        self._dao = dao
