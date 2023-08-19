
import random
from typing import List

from world import World

class CellWorld(World):
    def __init__(self, x_range, y_range):
        super().__init__(x_range, y_range)
        self.state = self._seed(self.x_range, self.y_range)

    def _seed(self, x_range: int, y_range: int) -> List[List[bool]]:
        state = [False] * y_range
        for row in range(y_range):
            state[row] = [False] * x_range
            for column in range(x_range):
                state[row][column] = (int(random.random()*10)) % 2 == 0
        return state

    def tick(self) -> List[List[bool]]:
        self.state = self._seed(self.x_range, self.y_range)
        return self.state.copy()
