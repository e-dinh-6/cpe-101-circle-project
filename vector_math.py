import data
from data import *


def scale_vector(vector: Vector, scalar):
    return Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)


def dot_vector(vector1: Vector, vector2: Vector):
    return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)


def length_vector(vector: Vector):
    return (vector.x ** 2 + vector.y ** 2 + vector.z **2) ** .5


def normalize_Vector(vectors: Vector):
    length = length_vector(vectors)
    return Vector(vectors.x/abs(length), vectors.y/abs(length), vectors.z/abs(length))


def difference_point(point1: Point, point2: Point):
    return Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)


def difference_vector(vector1: Vector, vector2: Vector):
    return Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)


def translate_point(point: Point, vector: Vector):
    return Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)


def vector_from_to(from_point: Point, to_point: Point):
    return Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)

