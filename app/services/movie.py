"""
    Service abstraction level
    Movie service class
"""

from .base import BaseService
from app.dao import MovieDAO


class MovieService(BaseService[MovieDAO]):
    def __init__(self, dao: MovieDAO):
        self._dao = dao
