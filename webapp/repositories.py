from contextlib import AbstractContextManager
from typing import List, Callable

from sqlalchemy.orm import Session

from .models import User


class UserRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self._session_factory = session_factory

    def get_all(self) -> List[User]:
        with self._session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, id: int) -> User:
        with self._session_factory() as session:
            user = session.query(User).filter(User.id == id).first()
            if not user:
                raise UserNotFoundError(id)
            return user

    def add_user(self, email: str, password: str, is_active: bool = True) -> User:
        with self._session_factory() as session:
            user = User(email=email, hashed_password=password, is_active=is_active)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_user_by_id(self, id: int) -> None:
        with self._session_factory() as session:
            user = session.query(User).filter(User.id == id).first()
            if not user:
                raise UserNotFoundError(id)
            session.delete(user)
            session.commit()


class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):
    entity_name: str = "User"
