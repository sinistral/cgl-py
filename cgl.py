
from cell_world import CellWorld
from engine import Engine

WORLD_CELLS_X = 100
WORLD_CELLS_Y = 100

Engine(CellWorld(WORLD_CELLS_X, WORLD_CELLS_Y), grid_colour="", tick_period_ms=250).run()
