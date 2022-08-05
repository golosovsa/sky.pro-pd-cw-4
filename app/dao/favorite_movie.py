"""
    DAO abstraction level
    Favorite movies DAO class
"""
from typing import Optional
from flask_sqlalchemy import BaseQuery

from .base import BaseDAO, T
from .models import FavoriteMovies
from werkzeug.exceptions import NotFound


class FavoriteMovieDAO(BaseDAO[FavoriteMovies]):
    __model__ = FavoriteMovies
    __updatable_fields__ = [
        "user_id",
        "movie_id",
    ]

    def get_all_by_user_id(self, user_id: int, page: Optional[int] = None) -> Optional[FavoriteMovies]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        stmt = stmt.filter(FavoriteMovies.user_id == user_id)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def get_all_by_movie_id(self, movie_id: int, page: Optional[int] = None) -> Optional[FavoriteMovies]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        stmt = stmt.filter(FavoriteMovies.movie_id == movie_id)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def get_by_ids(self, user_id: int, movie_id: int) -> FavoriteMovies:
        return self.get_by_id((user_id, movie_id))
