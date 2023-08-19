
import datetime
import tkinter

from world import World


class Engine:

    def __init__(self,
                 world: World,
                 origin_x=10, origin_y=10,
                 grid_colour="lightgrey",
                 cell_w=5, cell_h=5,
                 cell_padding=1,
                 tick_period_ms=300):
        self._root = tkinter.Tk()
        self._root.title("cgl")
        self._root.geometry("500x500")

        self._canvas = tkinter.Canvas(self._root, width=800, height=800, bg="white")
        self._canvas.pack()

        self._world = world
        self._grid_colour = grid_colour

        self._origin_x = origin_x
        self._origin_y = origin_y
        self._cell_width = cell_w
        self._cell_height = cell_h
        self._cell_padding = cell_padding
        self._tick_period_ms = tick_period_ms

        self._rect_offset_x = self._cell_width + (self._cell_padding*2)
        self._rect_offset_y = self._cell_height + (self._cell_padding*2)

    def _draw_grid(self):
        min_x = self._origin_x
        max_x = self._origin_x + self._world.x_range*(self._cell_width+(self._cell_padding*2))
        min_y = self._origin_y
        max_y = self._origin_y + self._world.y_range*(self._cell_height+(self._cell_padding*2))

        for horizontal in range(self._world.y_range+1):
            y = horizontal * self._rect_offset_y
            self._canvas.create_line(min_x, self._origin_y+y, max_x, self._origin_y+y, fill=self._grid_colour)

        for vertical in range(self._world.x_range+1):
            x = vertical * self._rect_offset_x
            self._canvas.create_line(self._origin_x+x, min_y, self._origin_x+x, max_y, fill=self._grid_colour)

    def _cell_rect(self, cell_x, cell_y):
        rect_x1 = self._origin_x + (cell_x*self._rect_offset_x) + self._cell_padding
        rect_y1 = self._origin_y + (cell_y*self._rect_offset_y) + self._cell_padding
        rect_x2 = self._origin_x + (cell_x*self._rect_offset_x) + self._cell_width + self._cell_padding
        rect_y2 = self._origin_y + (cell_y*self._rect_offset_y) + self._cell_height + self._cell_padding
        return [rect_x1, rect_y1, rect_x2, rect_y2]

    def _draw_cells(self):
        world_view = self._world.tick()
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
        self._canvas.after(self._tick_period_ms, self._animloop)

    def run(self):
        self._canvas.after(self._tick_period_ms, self._animloop)
        self._root.mainloop()
