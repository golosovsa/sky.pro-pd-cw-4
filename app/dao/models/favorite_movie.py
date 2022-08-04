"""
    FavoriteMovies SQLAlchemy model
"""

from sqlalchemy import Column, ForeignKey, BigInteger

from app.setup.db.models import BaseManyToMany


class FavoriteMovies(BaseManyToMany):
    __tablename__ = "favorite_movies"

    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    movie_id = Column(BigInteger, ForeignKey("movies.id", ondelete="CASCADE"), primary_key=True)
