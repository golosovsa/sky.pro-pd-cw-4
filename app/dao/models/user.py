"""
    Users SQLAlchemy model
"""

from sqlalchemy import Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from app.setup.db.models import BaseWithID, KeyType


class User(BaseWithID):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String(40))
    surname = Column(String(40))
    favorite_genre_id = Column(KeyType, ForeignKey("genres.id"))
    # many to one
    favorite_genre = relationship("Genre")
    # maby to many
    favorite_movies = relationship("Movie", secondary="favorite_movies")

