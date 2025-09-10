from my_project.external.repository.interface import AbstractRepository


class DBRepository(AbstractRepository):
    def __init__(self, *, db_session):
        self._db_session = db_session
        
    async def get(self, *, id: int):
        ...
