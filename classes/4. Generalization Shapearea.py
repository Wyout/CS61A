"""Generalization 1"""
from math import pi, sqrt
def area(r, shape_constant):
    assert r > 0, 'r必须大于0'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)
