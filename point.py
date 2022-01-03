import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Point) and __o.x == self.x and __o.y == self.y

    def __str__(self) -> str:
        return f"({int(self.x)}, {int(self.y)})"

    def __repr__(self) -> str:
        return self.__str__()

    def move(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def coordinate(self):
        return self.x, self.y

    def rotate(self, center, angle: int):
        x = math.cos(angle) * (self.x-center.x) - \
            math.sin(angle) * (self.y-center.y) + center.x
        y = math.sin(angle) * (self.x-center.x) + \
            math.cos(angle) * (self.y-center.y) + center.y
        return self.__class__(x, y)
