from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def masofani_hisobla(point1, point2):
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

p1 = Point(1, 2)
p2 = Point(4, 6)

print(masofani_hisobla(p1, p2))
