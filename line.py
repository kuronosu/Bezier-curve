import pygame
from point import Point
from colors import WHITE

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end
        self.dx = ((self.end.x - self.start.x) / 100)
        self.dy = ((self.end.y - self.start.y) / 100)

    def __str__(self) -> str:
        return f'Line({self.start},{self.end})'

    def __repr__(self) -> str:
        return str(self)

    def display(self, screen, color=WHITE):
        pygame.draw.line(
            screen, color, self.start.coordinate(), self.end.coordinate())

    def __call__(self, time: int) -> Point:
        return Point(self.start.x + self.dx*time, self.start.y + self.dy*time)