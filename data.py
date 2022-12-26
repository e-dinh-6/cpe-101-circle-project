#
# Name: Emi Dinh
# Instructor: Hisham H. Assal
# Section: CPE 101
# contains your class definitions with __init__
#

from utility import *


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)


class Ray:
    def __init__(self, pt: Point, dir: Vector):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return epsilon_equal(self.pt, other.pt) and epsilon_equal(self.dir, other.dir)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return epsilon_equal(self.r, other.r) and epsilon_equal(self.g, other.g) and epsilon_equal(self.b, other.b)


class Finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        return epsilon_equal(self.ambient, other.ambient) and \
               epsilon_equal(self.diffuse, other.diffuse) and \
               epsilon_equal(self.specular, other.specular) and \
               epsilon_equal(self.roughness, other.roughness)


class Light:
    def __init__(self, pt: Point, color: Color):
        self.pt = pt
        self.color = color

    def __eq__(self, other):
        return epsilon_equal(self.pt, other.pt) and epsilon_equal(self.color, other.color)


class Sphere:
    def __init__(self, center: Point, radius, color: Color, finish: Finish):
        self.center = center
        self.radius = float(radius)
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius
