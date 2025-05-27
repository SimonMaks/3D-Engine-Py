from points import Point_2D, Point_3D

class Line_2D:
    def __init__(self, start: Point_2D, end: Point_2D):
        self.start = start
        self.end = end

class Line_3D:
    def __init__(self, start: Point_3D, end: Point_3D):
        self.start = start
        self.end = end
