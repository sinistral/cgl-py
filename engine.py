
import datetime
import tkinter

from world import World

ORIGIN_X = 10
ORIGIN_Y = 10

CELL_W = 5
CELL_H = 5
CELL_PADDING = 1

class Engine:

    def __init__(self, world: World):
        self._root = tkinter.Tk()
        self._root.title("cgl")
        self._root.geometry("500x500")

        self._canvas = tkinter.Canvas(self._root, width=800, height=800, bg="white")
        self._canvas.pack()

        self.world = world

    def _draw_grid(self):
        min_x = ORIGIN_X
        max_x = ORIGIN_X + self.world.x_range*(CELL_W+(CELL_PADDING*2))
        min_y = ORIGIN_Y
        max_y = ORIGIN_Y + self.world.y_range*(CELL_H+(CELL_PADDING*2))

        for horizontal in range(self.world.y_range+1):
            y = horizontal * (CELL_H + (CELL_PADDING*2))
            self._canvas.create_line(min_x, ORIGIN_Y+y, max_x, ORIGIN_Y+y, fill="black")

        for vertical in range(self.world.x_range+1):
            x = vertical * (CELL_W + (CELL_PADDING*2))
            self._canvas.create_line(ORIGIN_X+x, min_y, ORIGIN_X+x, max_y, fill="black")

    def _cell_rect(self, cell_x, cell_y):
        rect_x1 = ORIGIN_X + (cell_x*(CELL_W + (CELL_PADDING*2))) + CELL_PADDING
        rect_y1 = ORIGIN_Y + (cell_y*(CELL_H + (CELL_PADDING*2))) + CELL_PADDING
        rect_x2 = ORIGIN_X + (cell_x*(CELL_W + (CELL_PADDING*2))) + CELL_W + CELL_PADDING
        rect_y2 = ORIGIN_Y + (cell_y*(CELL_H + (CELL_PADDING*2))) + CELL_H + CELL_PADDING
        return [rect_x1, rect_y1, rect_x2, rect_y2]

    def _draw_cells(self):
        world_view = self.world.tick()
        x_range = len(world_view)
        y_range = len(world_view[0])

        for y in range(y_range):
            for x in range(x_range):
                if world_view[x][y]:
                    self._canvas.create_rectangle(self._cell_rect(x, y), fill="red", outline="black", width=1)

    def _animloop(self):
        self._canvas.delete(tkinter.ALL)
        self._draw_grid()
        self._draw_cells()
        self._canvas.after(500, self._animloop)

    def run(self):
        self._canvas.after(500, self._animloop)
        self._root.mainloop()
