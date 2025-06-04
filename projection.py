from camera import Camera
from points import Point_2D, Point_3D
from lines import Line_2D, Line_3D
import math

class Projection:
    def __init__(self, screen_width, screen_height, fov, camera: Camera):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fov = fov
        self.camera = camera

    def project_point(self, point: Point_3D) -> Point_2D:
        middle_scr_x = round(self.screen_width / 2)
        middle_scr_y = round(self.screen_height / 2)
        dis_to_scr = self.camera.distance_to_screen

        dx = point.x - self.camera.position.x
        dy = point.y - self.camera.position.y
        dz = point.z - self.camera.position.z

        cos_yaw = math.cos(self.camera.yaw)
        sin_yaw = math.sin(self.camera.yaw)
        xz = dx * cos_yaw - dz * sin_yaw
        zz = dx * sin_yaw + dz * cos_yaw

        cos_pitch = math.cos(self.camera.pitch)
        sin_pitch = math.sin(self.camera.pitch)
        yz = dy * cos_pitch - zz * sin_pitch
        zz = dy * sin_pitch + zz * cos_pitch 

        if zz >= 0:
            return Point_2D(middle_scr_x, middle_scr_y)

        scale = dis_to_scr / -zz
        proj_x = round(middle_scr_x + xz * scale)
        proj_y = round(middle_scr_y - yz * scale)

        return Point_2D(proj_x, proj_y)


    def project_line(self, line: Line_3D) -> Line_2D:
        start_2d = self.project_point(line.start)
        end_2d = self.project_point(line.end)
        return Line_2D(start_2d, end_2d)
