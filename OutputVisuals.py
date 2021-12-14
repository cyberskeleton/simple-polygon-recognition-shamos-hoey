import tkinter as tk
from Point import Point

def draw_polygon(poly):
    width = 500
    height = 500
    border = 25

    max_x = 0
    max_y = 0
    for seg in poly:
        if seg.start.x > max_x:
            max_x = seg.start.x
        if seg.start.y > max_y:
            max_y = seg.start.y
    scale_x = (width - 2 * border) / max_x if max_x != 0 else 1
    scale_y = (height - 2 * border) / max_y if max_y != 0 else 1
    scale = scale_x if scale_x < scale_y else scale_y
    #print("scale: ", scale)

    #root = tk.Toplevel()
    vertices = []
    to_draw = []
    for segment in poly:
        if segment.start not in vertices:
            vertices.append(segment.start)
            point = Point(segment.start.x * scale + border, segment.start.y * scale + border)
            to_draw.append(point)
            #print(segment.print())
    # for i in vertices:
    #     print(i.x, i.y)

    c = tk.Canvas(bg="white", width=width, height=height)
    c.pack()
    out = []
    for point in to_draw:
        out.append([point.x * 1, point.y * 1])
    c.create_polygon(*out, fill="", outline="black")
    c.update()
    #root.mainloop()
