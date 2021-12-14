import math
from Segment import Segment
from Point import Point


class SweepLine:

    def __init__(self):
        self.position_x = -math.inf
        self.pool = []
        self.count = 0

    def move(self, next):
        self.above = None
        self.below = None
        self.position_x = next.x
        segment = next.segment
        if segment.end == next and segment in self.pool:
            self.pool.remove(segment)
        self.insert(segment)
        if self.intersects(segment):
            return True
        return False

    def insert(self, segment):
        entries = len(self.pool)
        if entries == 0:
            self.pool.append(segment)
            return
        for seg in self.pool:
            self.count += 1
            if seg.start.y > segment.start.y and (self.above == None or self.above.start.y > seg.start.y):
                self.above = seg
            elif self.below == None or self.below.start.y < seg.start.y:
                self.below = seg

    def intersects(self, segment):
        if (self.above and segment.intersects(self.above)) or (self.below and segment.intersects(self.below)):
            return True
        return False

    def counter(self):
        return self.count