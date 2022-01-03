
import sys
from typing import List, Tuple

import pygame

from animation import Animation
from bezier import Bezier
from colors import BLACK
from figures import heart1, heart2
from utils import draw_figure


def main(width=700, height=700, figures=[], animations: List[Tuple[Bezier, bool]] = [], fps=60):
    pygame.init()
    pygame.display.set_caption('Bézier curve')

    size = width, height
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    animations: List[Animation] = [
        Animation(screen, B, loop) for B, loop in animations]

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(BLACK)

        for animation in animations:
            animation.tick()
        for B in figures:
            draw_figure(screen, B)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    width, height = 700, 700
    animation_time = 2  # 17
    fps = 60  # 100 / segment_length

    heart = heart2(width, height)

    figures = [heart[0]]
    animations = [(heart[1], True)]
    main(figures=figures, animations=animations, fps=fps)
