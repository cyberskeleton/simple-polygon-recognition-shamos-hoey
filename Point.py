class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.segment = None
        self.is_start = False
        self.is_end = False

    def set_segment(self, segment):
        self.segment = segment

    def get_segment(self):
        return self.segment

    def compare(self, point2):
        if self.x == point2.x:
            if self.y == point2.y:
                return self.compare_by_segments(point2)
            elif self.y < point2.y:
                return -1
            else:
                return 1
        elif self.x < point2.x:
            return -1
        else:
            return 1

    def compare_by_segments(self, point2):
        if self.is_start:
            if point2.is_end:
                return -1
        elif self.is_end:
            if point2.is_start:
                return 1
        return 0

    def print(self):
        return "<x:{x}, y:{y}, segment:{s} {p}>".format(x=self.x, y=self.y,
                                                        s=self.segment.print() if self.segment is not None else "",
                                                        p=("start" if self.is_start else("end" if self.is_end else "")))

