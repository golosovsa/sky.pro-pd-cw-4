from flask_restx import Namespace, Resource

from app.container import favorite_movie_service, user_service
from app.setup.api.models import favorite_movie_schema
from app.setup.api.parsers import page_parser
from app.tools.security import login_required

api = Namespace('favorites', description="Любимые фильмы")


@api.route('/movies/')
class FavoriteMoviesView(Resource):
    @login_required
    @api.expect(page_parser)
    @api.marshal_with(favorite_movie_schema, as_list=True, code=200, description='OK')
    def get(self, movie_id, user_token):
        """
        Get all favorite movies.
        """
        user = user_service.get(user_token)
        return favorite_movie_service.get_all_by_user_id(user.id, **page_parser.parse_args())


@api.route('/movies/<int:movie_id>')
class FavoriteMovieView(Resource):
    @login_required
    @api.marshal_with(favorite_movie_schema, code=200, description='OK')
    def get(self, movie_id, user_token):
        """
        Get one favorite movie.
        """
        user = user_service.get(user_token)
        return favorite_movie_service.get_item((user.id, movie_id,))

    @login_required
    def post(self, movie_id, user_token):
        user = user_service.get(user_token)
        favorite_movie_service.create({
            "user_id": user.id,
            "movie_id": movie_id
        })
        return "OK", 201, {"Location": f"/movies/{movie_id}"}

    @login_required
    def delete(self, movie_id, user_token):
        user = user_service.get(user_token)
        favorite_movie_service.delete((user.id, movie_id,))
        return "OK", 204
