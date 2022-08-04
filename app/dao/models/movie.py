"""
    Movies SQLAlchemy model
"""

from sqlalchemy import Column, String, Text, Integer, Numeric, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from app.setup.db.models import BaseWithID


class Movie(BaseWithID):
    __tablename__ = 'movies'

    title = Column(String(100), nullable=False)
    description = Column(Text)
    trailer = Column(String(100))
    year = Column(Integer)
    rating = Column(Numeric(2, 2))
    genre_id = Column(BigInteger, ForeignKey("genres.id"))
    director_id = Column(BigInteger, ForeignKey("directors.id"))
    # many to one
    genre = relationship("Genre", back_populates="movies")
    # many to one
    director = relationship("Director", back_populates="movies")
