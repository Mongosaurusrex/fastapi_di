from dependency_injector import containers, providers

from .database import Database
from .repositories import UserRepository
from .services import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    db = providers.Singleton(
        Database, db_url="postgresql://postgres:supersecret@localhost/fastapi"
    )

    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )

    user_service = providers.Factory(UserService, user_repository=user_repository)
