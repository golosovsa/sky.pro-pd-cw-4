from flask_restx import Namespace, Resource

from app.container import favorite_movie_service, user_service
from app.setup.api.models import favorite_movie_schema
from app.setup.api.parsers import page_parser

api = Namespace('favorites', description="Любимые фильмы")


@api.route('/movies/<int:movie_id>')
class FavoriteMoviesView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(favorite_movie_schema, as_list=True, code=200, description='OK')
    def get(self, movie_id):
        """
        Get all directors.
        """
        return favorite_movie_service.get_all_by_movie_id(movie_id, **page_parser.parse_args())


@api.route('/users/<int:user_id>/')
class FavoriteMovieView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(favorite_movie_schema, as_list=True, code=200, description='OK')
    def get(self, user_id: int):
        """
        Get director by id.
        """
        return favorite_movie_service.get_all_by_user_id(user_id, **page_parser.parse_args())
