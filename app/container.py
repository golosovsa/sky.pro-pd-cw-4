from app.dao import GenreDAO, DirectorDAO, MovieDAO, UserDAO, FavoriteMovieDAO

from app.services import GenreService, DirectorService, MovieService, UserService, FavoriteMovieService
from app.setup.db import db

# DAO
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)
favorite_movie_dao = FavoriteMovieDAO(db.session)

# Services
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
favorite_movie_service = FavoriteMovieService(dao=favorite_movie_dao)
