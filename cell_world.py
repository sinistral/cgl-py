
import random
from typing import List

from world import World

class CellWorld(World):
    def __init__(self, x_range, y_range):
        super().__init__(x_range, y_range)
        self._state = self._seed(self.x_range, self.y_range)

    def _neighbours(self, x: int, y: int, state: List[List[int]]) -> List[bool]:
        """Returns the states of all neighbours of the cell at [x, y] as a List.  Detection wraps around world edges, so
        the EAST neighbour of [max(x), _] is considered to be [0, _].

        """
        def n(y):
            return self.y_range - 1 if y == 0 else y - 1
        def e(x):
            return 0 if x == self.x_range - 1 else x + 1
        def s(y):
            return 0 if y == self.y_range -1 else y + 1
        def w(x):
            return self.x_range - 1 if x == 0 else x - 1
        return list(map(lambda coord: self._state[coord[0]][coord[1]],
                        [
                            # nw
                            [w(x), n(y)],
                            # n
                            [x, n(y)],
                            # ne
                            [e(x), n(y)],
                            # e
                            [e(x), y],
                            # se
                            [e(x), s(y)],
                            # s
                            [x, s(y)],
                            # sw
                            [w(x), s(y)],
                            # w
                            [w(x), y]
                        ]))


    def _seed(self, x_range: int, y_range: int) -> List[List[bool]]:
        state = [False] * y_range
        for row in range(y_range):
            state[row] = [False] * x_range
            for column in range(x_range):
                state[row][column] = (int(random.random()*10)) % 2 == 0
        return state

    def tick(self) -> List[List[bool]]:
        next_generation_state = [False] * self.y_range
        for row in range(self.y_range):
            next_generation_state[row] = [False] * self.x_range
        for y in range(self.y_range):
            for x in range(self.x_range):
                live_neighbours_n = len(list(filter(lambda x: x, self._neighbours(x, y, self._state))))
                if self._state[x][y] and (live_neighbours_n == 2 or live_neighbours_n == 3):
                    # live cell that continues to live in the next generation
                    # print(f"{[x, y]} survives")
                    next_generation_state[x][y] = True
                elif not self._state[x][y] and live_neighbours_n == 3:
                    # reproduction replaces/populates a previously dead cell
                    # print(f"{[x, y]} spawns")
                    next_generation_state[x][y] = True
                else:
                    # print(f"{[x, y]} dies")
                    next_generation_state[x][y] = False
        # print(f"current: {self._state}")
        # print(f"next:    {next_generation_state}")
        self._state = next_generation_state
        return self._state.copy()
