import math
from typing import List

import pygame

from bezier import Bezier
from colors import BLUE, CYAN, GREEN, ORANGE, RED, WHITE
from point import Point


def mirror_vertical(points: List[Point], w):
    new_points = []
    for p in points:
        new_points.append(p.rotate(Point(w/2, p.y), math.pi))
    return new_points


def mirror_horizontal(points: List[Point], h):
    new_points = []
    for p in points:
        new_points.append(p.rotate(Point(p.x, h/2), math.pi))
    return new_points


def draw_figure(screen, figure: Bezier):
    points = figure()
    if len(points) == 0:
        return
    prev = points[0]
    for cur in points[1:]:
        pygame.draw.line(
            screen, figure.color, prev[0].coordinate(), cur[0].coordinate())
        prev = cur


def coordinates_to_pixel(coordinates, w, h):
    h = h - 2*(h/8)
    w = w - 2*(w/8)
    lm, rm = w/8, w/8
    Xmin = min(coordinates, key=lambda c: c[0])[0]
    Ymin = min(coordinates, key=lambda c: c[1])[1]
    Xmax = max(coordinates, key=lambda c: c[0])[0]
    Ymax = max(coordinates, key=lambda c: c[1])[1]
    points = []
    for x, y in coordinates:
        points.append(Point(
            lm + (x-Xmin) / (Xmax-Xmin) * w,
            rm + h - (y-Ymin) / (Ymax-Ymin) * h))
    return points


def get_deep_color(deep):
    COLORS = [RED, GREEN, BLUE, ORANGE, CYAN, WHITE]
    return COLORS[deep if deep < len(COLORS) else deep % len(COLORS)]
