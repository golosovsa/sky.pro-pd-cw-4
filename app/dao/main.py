from app.dao.base import BaseDAO
from app.models import Genre


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre
