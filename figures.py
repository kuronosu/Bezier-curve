from bezier import Bezier
from colors import RED
from point import Point
from utils import coordinates_to_pixel, mirror_vertical


def heart1(width, height):
    points = [[5, 0], [0, 2], [0, 10], [6, 10], [14, -2],
              [-4, -2], [4, 10], [10, 10], [10, 2], [5, 0]]

    PS, *references, PE = coordinates_to_pixel(points, width, height)
    return [Bezier(PS, PE, *references)]


def heart2(width, height):
    PS = Point(width/2, height/3)
    PE = Point(width/2, (height/3) * 2)
    references = [
        Point(width/2, height/6),
        Point(width/3, height/8),
        Point(width/7, height/6),
        Point(width/7, (height/6)*3),
    ]
    B = Bezier(PS, PE, *references, color=RED)
    B2 = Bezier(PS, PE, *mirror_vertical(references, width), color=RED)
    return [B, B2]
