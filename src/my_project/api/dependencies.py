"""
Module containing dependencies for the FastAPI dependency injection functions.
They will be used in the API routes and other dependency functions.
"""
from typing import Annotated

from fastapi import Depends

from my_project.external import resources
from my_project.external.repository.db import DBRepository
from my_project.external.repository.interface import AbstractRepository
from src.my_project.services.service import Service


def get_repository() -> AbstractRepository:
    return DBRepository(db_session=resources.get_db_session())


def get_service(repository: Annotated[AbstractRepository, Depends[get_repository]]) -> Service:
    return Service(repository=repository)

