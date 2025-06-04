import math
from points import Point_3D

class Camera:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = Point_3D(0, 0, 100)
        self.yaw = 0
        self.pitch = 0
        self.distance_to_screen = round(math.sqrt(3) * screen_width / 2)
