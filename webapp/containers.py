from dependency_injector import containers, providers

from .database import Database


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(
        Database, db_url="postgresql://postgres:supersecret@localhost/fastapi"
    )
