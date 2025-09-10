from abc import ABC, abstractmethod
from typing import Any


class AbstractRepository(ABC):
    @abstractmethod
    async def get(self, *, id: int):
        raise NotImplementedError
