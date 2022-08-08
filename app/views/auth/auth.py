from flask_restx import Namespace, Resource
from flask import request

api = Namespace('auth', description="User authentication")

from app.container import user_service


@api.route("/register/")
class AuthRegistrationView(Resource):
    @api.response(400, "Bad request")
    def post(self):
        data = request.json
        user = user_service.register(data)
        return "OK", 201,  {'location': f'/users/{user.id}'}


@api.route("/login/")
class AuthRegistrationView(Resource):
    @api.response(400, "Bad request")
    def post(self):
        data = request.json
        return user_service.login(data), 200

    @api.response(400, "Bad request")
    def put(self):
        refresh_token = request.form.get("refresh_token", None)
        return user_service.refresh(refresh_token)

