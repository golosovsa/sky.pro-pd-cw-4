from app.dao import GenresDAO

from app.services import GenresService
from app.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
