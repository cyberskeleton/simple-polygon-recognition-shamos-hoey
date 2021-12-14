class Segment:
    def __init__(self, start_point, end_point):
        self.start = start_point
        start_point.is_start = True
        self.end = end_point
        end_point.is_end = True
        start_point.segment = self
        end_point.segment = self

    def intersects(self, another):
        # print("Comparing: ", self.print(), " vs ", another.print())
        # edges of the same vertex
        if (self.start.x == another.end.x) and (self.start.y == another.end.y):
            return False
        if (self.end.x == another.start.x) and (self.end.y == another.start.y):
            return False
        return self.segments_intersect(self.start, self.end, another.start, another.end)

    def segments_intersect(self, a, b, c, d):
        return self.ccw(a, c, d) != self.ccw(b, c, d) and self.ccw(a, b, c) != self.ccw(a, b, d)

    # https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
    def ccw(self, a, b, c):
        return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

    def print(self):
        return "({x1}:{y1}, {x2}:{y2})".format(x1=self.start.x, y1=self.start.y, x2=self.end.x, y2=self.end.y)

    def compare(self, segment):
        if self.start < segment.start:
            return -1
        elif self.start == segment.start:
            return 0
        return 1
