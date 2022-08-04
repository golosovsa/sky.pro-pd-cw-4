"""
    Service abstraction level
    User service class
"""

from .base import BaseService
from app.dao import UserDAO


class UserService(BaseService[UserDAO]):
    def __init__(self, dao: UserDAO):
        self._dao = dao
