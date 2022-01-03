from typing import Dict, List, Tuple

from colors import WHITE
from line import Line
from point import Point

BezierPoint = Tuple[Point, Dict[int, List[Line]]]


class BezierLine:

    def __init__(self, line1: Line, line2: Line) -> None:
        self.line1 = line1
        self.line2 = line2

        self.dl1 = ((self.line1.end.x - self.line1.start.x) / 100,
                    (self.line1.end.y - self.line1.start.y) / 100)

        self.dl2 = ((self.line2.end.x - self.line2.start.x) / 100,
                    (self.line2.end.y - self.line2.start.y) / 100)

    def __call__(self, time) -> Line:
        p1 = self.line1.start.move(self.dl1[0]*time, self.dl1[1]*time)
        p2 = self.line2.start.move(self.dl2[0]*time, self.dl2[1]*time)
        return Line(p1, p2)


class Bezier:
    def __init__(self, start: Point, end: Point, *references: Point, color=WHITE) -> None:
        self.start = start
        self.end = end
        self.references = list(references)
        self.deep = len(references)
        self.color = color
        self.lines = self.assembly_lines()
        self.result: List[BezierPoint] = None

    def _time(self, time) -> BezierPoint:
        tmp = self.lines
        lines: Dict[int, List[Line]] = {}
        for _ in range(self.deep+1):
            _tmp = self.reduce(time, tmp)
            if _tmp is None:
                return tmp[0](time), lines
            tmp = lines[_] = _tmp

    def __iter__(self):
        return BezierIterator(self)

    def __call__(self):
        if self.result is None:
            self.result = [it for it in self.__iter__()]
        return self.result

    def assembly_lines(self):
        lines = []
        prev = self.start
        for curr in self.references + [self.end]:
            lines.append(Line(prev, curr))
            prev = curr
        return lines

    def reduce(self, time, lines: List[Line]) -> List[Line] | None:
        if len(lines) <= 1:
            return None
        prev = lines[0]
        new_lines = []
        for line in lines[1:]:
            lb = BezierLine(prev, line)
            new_line = lb(time)
            new_lines.append(new_line)
            prev = line
        return new_lines

    def get_lines(self) -> List[Line]:
        points = self.references + [self.end]
        prev = self.start
        tmp = []
        for curr in points:
            tmp.append(Line(prev, curr))
            prev = curr
        return tmp


class BezierIterator:
    def __init__(self, bezier: Bezier, accuracy: int = 1) -> None:
        self.bezier = bezier
        self.accuracy = accuracy
        self.c: int = 0

    def __next__(self):
        if self.c > 100:
            raise StopIteration()
        p = self.bezier._time(self.c)
        self.c += self.accuracy
        return p

    def __iter__(self):
        return self
