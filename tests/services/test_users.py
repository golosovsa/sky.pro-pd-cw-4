from unittest.mock import MagicMock
import pytest

from app.dao import UserDAO
from app.exceptions import ItemNotFound, BadRequestData
from app.dao.models import User
from app.services import UserService


class TestUsersService:

    @pytest.fixture()
    def users_dao_mock(self):
        users = {
            1: User(
                id=1,
                email="test_user_1_email",
                password='test_user_1_password',
                name='test_user_1_name',
                surname='test_user_1_surname',
                favorite_genre_id=1,
            ),
            2: User(
                id=2,
                email="test_user_2_email",
                password='test_user_2_password',
                name='test_user_2_name',
                surname='test_user_2_surname',
                favorite_genre_id=2,
            ),
            3: User(
                id=3,
                email="test_user_3_email",
                password='test_user_3_password',
                name='test_user_3_name',
                surname='test_user_3_surname',
                favorite_genre_id=3,
            ),
            4: User(
                id=4,
                email="test_user_4_email",
                password='test_user_4_password',
                name='test_user_4_name',
                surname='test_user_4_surname',
                favorite_genre_id=4,
            ),
        }

        def create(model):
            model.id = max(users.keys()) + 1
            users[model.id] = model
            return model

        def delete(model):
            del users[model.id]

        dao = UserDAO(None)

        dao.get_by_id = MagicMock(side_effect=users.get)
        dao.get_all = MagicMock(return_value=list(users.values()))
        dao.create = MagicMock(side_effect=create)
        dao.update = dao.create
        dao.delete = MagicMock(side_effect=delete)

        return dao

    @pytest.fixture()
    def users_service(self, users_dao_mock):
        return UserService(dao=users_dao_mock)

    def test_get_user(self, users_service):
        model = users_service.get_item(1)
        assert model
        assert model.id == 1
        assert model.email == "test_user_1_email"
        assert isinstance(model, User)

    def test_user_not_found(self, users_dao_mock, users_service):
        with pytest.raises(ItemNotFound):
            users_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_users(self, users_dao_mock, users_service, page):
        users = users_service.get_all(page=page)
        assert len(users) == 4
        assert users == users_dao_mock.get_all.return_value
        users_dao_mock.get_all.assert_called_with(page=page)

    def test_create(self, users_service):
        model = users_service.create(
            {
                "email": 'test_user_5_email',
                "password": 'test_user_5_password',
                "name": 'test_user_5_name',
                "surname": 'test_user_5_surname',
                "favorite_genre_id": 5,
            })
        assert model
        assert users_service.get_item(model.id)
        assert users_service.get_item(model.id).email == "test_user_5_email"

    def test_create_bad_data(self, users_service):
        with pytest.raises(BadRequestData):
            users_service.create({"bad_key": "bad_value"})

    def test_update(self, users_service):
        model = users_service.update(1, {
            "email": 'test_user_1_email_update',
            "password": 'test_user_1_password_update',
            "name": 'test_user_1_name_update',
            "surname": 'test_user_1_surname_update',
            "favorite_genre_id": 11,
        })
        assert model
        assert model.email == "test_user_1_email_update"
        assert users_service.get_item(1).email == "test_user_1_email_update"

    def test_update_bad_data(self, users_service):
        with pytest.raises(BadRequestData):
            users_service.update(1, {"bad_key": "bad_value"})

    def test_partially_update(self, users_service):
        model = users_service.partially_update(1, {
            "email": 'test_user_1_email_update',
        })
        assert model
        assert model.email == "test_user_1_email_update"
        assert users_service.get_item(1).email == "test_user_1_email_update"

    def test_partially_update_bad_data(self, users_service):
        with pytest.raises(BadRequestData):
            users_service.partially_update(1, {"bad_key": "bad_value"})

    def test_delete(self, users_service):
        users_service.delete(1)
        with pytest.raises(ItemNotFound):
            users_service.get_item(1)

