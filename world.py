
from abc import ABC, abstractmethod
from typing import List

class World(ABC):
    def __init__(self, x_range: int, y_range: int):
        self._x_range = x_range
        self._y_range = y_range

    @property
    def x_range(self) -> int:
        return self._x_range

    @property
    def y_range(self) -> int:
        return self._y_range

    @abstractmethod
    def tick(self) -> List[List[bool]]:
        pass
