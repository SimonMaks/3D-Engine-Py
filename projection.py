from camera import Camera
from points import Point_2D, Point_3D
from lines import Line_2D, Line_3D

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

        c_x, c_y, c_z = self.camera.position.x, self.camera.position.y, self.camera.position.z
        p_x, p_y, p_z = point.x, point.y, point.z

        if p_z >= c_z:
            return Point_2D(middle_scr_x, middle_scr_y)

        scale = dis_to_scr / (c_z - p_z)
        proj_x = round(middle_scr_x + (p_x - c_x) * scale)
        proj_y = round(middle_scr_y - (p_y - c_y) * scale)

        return Point_2D(proj_x, proj_y)

    def project_line(self, line: Line_3D) -> Line_2D:
        start_2d = self.project_point(line.start)
        end_2d = self.project_point(line.end)
        return Line_2D(start_2d, end_2d)