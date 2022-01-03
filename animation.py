import pygame
from pygame.surface import Surface
from bezier import Bezier
from colors import WHITE
from utils import get_deep_color


class Animation:
    def __init__(self, screen: Surface, B: Bezier, loop: bool, show_references: bool = True) -> None:
        self._screen = screen
        self.B = B
        self.loop = loop
        self.show_references = show_references
        self.lines = B.get_lines()
        self.idx = 0

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, screen):
        self._screen = screen

    def tick(self):
        if self._screen == None:
            return

        if self.loop and self.idx >= len(self.B())-1:
            self.idx = 0

        self.draw_points()
        
        if self.show_references:
            for i in self.lines:
                i.display(self._screen, WHITE)
            bp = self.B()[self.idx]
            for idx, lines in bp[1].items():
                for line in lines:
                    line.display(self._screen, get_deep_color(idx))
        if self.idx + 1 < len(self.B()):
            self.idx += 1

    def draw_points(self):
        tmp = self.B()
        if len(tmp) == 0:
            return
        prev = tmp[0]
        for cur in tmp[1:self.idx]:
            pygame.draw.line(self._screen, self.B.color,
                             prev[0].coordinate(), cur[0].coordinate())
            prev = cur
