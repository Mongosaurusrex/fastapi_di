from uuid import uuid4
from typing import List

from .repositories import UserRepository
from .models import User


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def get_users(self) -> List[User]:
        return self._user_repository.get_all()

    def get_user_by_id(self, id: int) -> User:
        return self._user_repository.get_by_id(id)

    def create_user(self) -> User:
        uid = uuid4()
        return self._user_repository.add_user(email=f"{uid}@email.com", password="pwd")

    def delete_user_by_id(self, id: int) -> None:
        self._user_repository.delete_user_by_id(id)
