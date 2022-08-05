from flask_restx import Namespace, Resource

from app.container import favorite_movie_service, user_service
from app.setup.api.models import favorite_movie_schema
from app.setup.api.parsers import page_parser

api = Namespace('favorites', description="Любимые фильмы")


@api.route('/movies/')
class FavoriteMoviesView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(favorite_movie_schema, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        return favorite_movie_service.get_all(**page_parser.parse_args())


@api.route('/movies/<int:director_id>/')
class FavoriteMovieView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(favorite_movie_schema, code=200, description='OK')
    def get(self, director_id: int):
        """
        Get director by id.
        """
        return favorite_movie_service.get_item(director_id)
