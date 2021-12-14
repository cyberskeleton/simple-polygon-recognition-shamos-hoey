import math
import random
import re
import tkinter as tk
from EventQueue import EventQueue
from OutputVisuals import draw_polygon
from Point import Point
from Segment import Segment
from SweepLine import SweepLine

global auto
auto = False
global window


def build_polygon(argument):
    if type(argument) == str:
        vertices = [part.strip() for part in re.split('[()]', argument) if part.strip()]
        points_array = []
        for vertex in vertices:
            # print([int(i) for i in vertice.split(', ')])
            coords = [int(i) for i in vertex.split(', ')]
            p = Point(coords[0], coords[1])
            points_array.append(p)
    else:
        points_array = argument
    # print([p.print() for p in points_array])

    segments = []
    for i in range(0, len(points_array)-1):
        segment = Segment(Point(points_array[i].x, points_array[i].y), Point(points_array[i+1].x, points_array[i+1].y))
        segment.start.set_segment(segment)
        segment.start.is_start = True
        segment.end.set_segment(segment)
        segment.end.is_end = True
        segments.append(segment)

    last_to_first = Segment(points_array[len(points_array)-1], points_array[0])
    last_to_first.start.set_segment(last_to_first)
    last_to_first.end.set_segment(last_to_first)
    segments.append(last_to_first)
    # print([s.start.print() + "<->" + s.end.print() for s in segments])

    return segments

def input_polygon():
    top = tk.Toplevel()
    top.title("polygon")
    manual_label = tk.Label(top, text="input polygon's vertices in like this: (x1, y1) (x2, y2) ...")
    manual_label.pack()
    input_box = tk.Entry(top)
    input_box.pack()
    next_button = tk.Button(top, text="Next", command=lambda: next_input(top, input_box))
    next_button.pack()


def generate_polygon():
    number_of_vertices = random.randint(3, 100)
    vertices = []
    for i in range(number_of_vertices):
        x = random.randint(0, 50)
        y = random.randint(0, 50)
        vertices.append(Point(x, y))
    poly = build_polygon(vertices)
    run(poly)


def get_value(input_box, top, auto):
    n = input_box.get()
    print(n)
    top.destroy()
    if auto == False:
        #for i in range(int(n)):
        input_polygon()
    else:
        for i in range(int(n)):
            generate_polygon()

def input_number_of_polygons():
    top = tk.Toplevel()
    top.title("manual input")
    manual_label = tk.Label(top, text = "please input the number of polygons")
    manual_label.pack()
    input_box = tk.Entry(top)
    input_box.pack()
    ok_button = tk.Button(top, text = "OK", command = lambda : get_value(input_box, top, auto))
    ok_button.pack()

def next_input(win, input_box):
    global window
    m = input_box.get()
    #print(m)
    win.destroy()
    poly = build_polygon(m)
    #print(poly)\
    window.destroy()
    draw_polygon(poly)
    run(poly)


def manual_input():
    print("manual input selected")
    #input_number_of_polygons()
    input_polygon()

def auto_input():
    global auto
    auto = True
    print("auto input selected")
    input_number_of_polygons()


def create_UI():
    global window
    window = tk.Tk()
    window.title("simple polygon recognition")
    select_options = tk.Label(text = "Please select input mode", height = 3)
    select_options.pack()
    manual_button = tk.Button(window, text = "manual input", command = manual_input)
    auto_button = tk.Button(window, text="automatic input", command = auto_input)
    manual_button.pack()
    auto_button.pack()
    window.mainloop()


def run(segments):
    sweep_line = SweepLine()
    queue = EventQueue(segments, sweep_line, False)
    result = queue.has_intersections()
    if auto:
        if not result:
            vertices = len(segments)
            print(vertices, " vertices polygon does not self-intersect; ", sweep_line.counter()
                , " comparisons done; N*log(N)=", math.log(vertices) * vertices)
    else:
        print("polygon self-intersects: ", result)