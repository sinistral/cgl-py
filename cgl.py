
import datetime
import random
import tkinter

ORIGIN_X = 10
ORIGIN_Y = 10

WORLD_CELLS_X = 10
WORLD_CELLS_Y = 10

CELL_W = 10
CELL_H = 10
CELL_PADDING = 3

root = tkinter.Tk()

root.title("cgl")
root.geometry("500x500")

canvas = tkinter.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

min_x = ORIGIN_X
max_x = ORIGIN_X + WORLD_CELLS_X*(CELL_W+(CELL_PADDING*2))
min_y = ORIGIN_Y
max_y = ORIGIN_Y + WORLD_CELLS_Y*(CELL_H+(CELL_PADDING*2))

def draw_grid():
    for horizontal in range(WORLD_CELLS_Y+1):
        y = horizontal * (CELL_H + (CELL_PADDING*2))
        canvas.create_line(min_x, ORIGIN_Y+y, max_x, ORIGIN_Y+y, fill="black")
    for vertical in range(WORLD_CELLS_X+1):
        x = vertical * (CELL_W + (CELL_PADDING*2))
        canvas.create_line(ORIGIN_X+x, min_y, ORIGIN_X+x, max_y, fill="black")

draw_grid()

def cell_rect(cell_x, cell_y):
    rect_x1 = ORIGIN_X + (cell_x*(CELL_W + (CELL_PADDING*2))) + CELL_PADDING
    rect_y1 = ORIGIN_Y + (cell_y*(CELL_H + (CELL_PADDING*2))) + CELL_PADDING
    rect_x2 = ORIGIN_X + (cell_x*(CELL_W + (CELL_PADDING*2))) + CELL_W + CELL_PADDING
    rect_y2 = ORIGIN_Y + (cell_y*(CELL_H + (CELL_PADDING*2))) + CELL_H + CELL_PADDING
    return [rect_x1, rect_y1, rect_x2, rect_y2]

def draw_cells():
    max_range = int(random.random()*10)
    for i in range(0, max_range):
        canvas.create_rectangle(cell_rect(i, i), fill="red", outline="black", width=1)

def render_frame():
    draw_grid()
    draw_cells()

render_frame()

def animloop():
    canvas.delete(tkinter.ALL)
    render_frame()
    canvas.after(500, animloop)

canvas.after(500, animloop)
root.mainloop()
