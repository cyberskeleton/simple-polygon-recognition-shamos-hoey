from functools import cmp_to_key
from Point import Point

class EventQueue:
    def __init__(self, segments, sweep_line, debug):
        self.sweep_line = sweep_line
        self.points = []
        if debug == None:
            debug = False
        self.debug = debug
        for seg in segments:
            if seg.start.compare(seg.end) > 0:
                temp = seg.start
                seg.start = seg.end
                seg.start.is_start = True
                seg.start.is_end = False
                seg.end = temp
                seg.end.is_start = False
                seg.end.is_end = True
                # print("reverted:" + seg.start.print() + "; " + seg.end.print())
            self.points.append(seg.start)
            self.points.append(seg.end)
            if self.debug:
                print("In:" + seg.start.print() + "; " + seg.end.print())
        self.points.sort(key=cmp_to_key(Point.compare))
        if self.debug:
            print("Points: \n", '\n '.join("%s" % (item.print()) for item in self.points))

    def has_intersections(self):
        if len(self.points) < 2:
            return False
        for point in self.points:
            intersects = self.sweep_line.move(point)
            if self.debug:
                print(point.print(), " has intersections:", intersects)
            if intersects:
                return True
        return False

