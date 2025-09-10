from my_project.external.repository.interface import AbstractRepository


class Service:
    def __init__(
            self,
            repository: AbstractRepository
    ):
        self._repository = repository

    async def get_data(self, *, item_id: int):
        ...
        ... = await self._repository.get(id=item_id)
        return ...
