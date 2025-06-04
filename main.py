import pygame
from points import Point_2D, Point_3D
from lines import Line_2D, Line_3D
from projection import Projection
from camera import Camera
import math

class Application:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("3D Projection")
        self.clock = pygame.time.Clock()
        self.running = True
        self.camera = Camera(self.width, self.height)
        self.projection = Projection(self.width, self.height, 90, self.camera)

        self.points_3d = [
            Point_3D(-50, -50, -200), Point_3D(50, -50, -200),
            Point_3D(50, 50, -200), Point_3D(-50, 50, -200),
            Point_3D(-50, -50, -300), Point_3D(50, -50, -300),
            Point_3D(50, 50, -300), Point_3D(-50, 50, -300)
        ]

        self.lines_3d = [
            Line_3D(self.points_3d[0], self.points_3d[1]),
            Line_3D(self.points_3d[1], self.points_3d[2]),
            Line_3D(self.points_3d[2], self.points_3d[3]),
            Line_3D(self.points_3d[3], self.points_3d[0]),
            Line_3D(self.points_3d[4], self.points_3d[5]),
            Line_3D(self.points_3d[5], self.points_3d[6]),
            Line_3D(self.points_3d[6], self.points_3d[7]),
            Line_3D(self.points_3d[7], self.points_3d[4]),
            Line_3D(self.points_3d[0], self.points_3d[4]),
            Line_3D(self.points_3d[1], self.points_3d[5]),
            Line_3D(self.points_3d[2], self.points_3d[6]),
            Line_3D(self.points_3d[3], self.points_3d[7]),
        ]

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEWHEEL:
                zoom_speed = 10
                self.camera.position.z += -event.y * zoom_speed

        keys = pygame.key.get_pressed()
        move_speed = 5
        rotation_speed = math.radians(2) 

        if keys[pygame.K_LEFT]:
            self.camera.position.x -= move_speed
        if keys[pygame.K_RIGHT]:
            self.camera.position.x += move_speed
        if keys[pygame.K_UP]:
            self.camera.position.y += move_speed
        if keys[pygame.K_DOWN]:
            self.camera.position.y -= move_speed

        if keys[pygame.K_a]:
            self.camera.yaw -= rotation_speed
        if keys[pygame.K_d]:
            self.camera.yaw += rotation_speed
        if keys[pygame.K_w]:
            self.camera.pitch += rotation_speed
        if keys[pygame.K_s]:
            self.camera.pitch -= rotation_speed

    def draw(self):
        self.screen.fill((255, 255, 255))
        for line in self.lines_3d:
            line_2d = self.projection.project_line(line)
            pygame.draw.line(self.screen, (0, 0, 0),
                             (line_2d.start.x, line_2d.start.y),
                             (line_2d.end.x, line_2d.end.y), 2)
        pygame.display.flip()

if __name__ == "__main__":
    app = Application()
    app.run()
