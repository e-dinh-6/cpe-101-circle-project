import data
import math
from data import *
import vector_math
from vector_math import *


def sphere_intersection_point(ray: Ray, sphere: Sphere):
    a = dot_vector(ray.dir, ray.dir)
    b = 2 * dot_vector(difference_point(ray.pt, sphere.center), ray.dir)
    c = dot_vector(difference_point(ray.pt, sphere.center), difference_point(ray.pt, sphere.center)) - (
            sphere.radius ** 2)

    returnedRoot = quadratic(a, b, c)

    if returnedRoot is not None:
        return translate_point(ray.pt, scale_vector(ray.dir, returnedRoot))
    else:
        return None


def quadratic(a, b, c):
    quad_inside = b ** 2 - (4 * a * c)

    if quad_inside < 0:
        return None

    root1 = ((-b) + math.sqrt(quad_inside)) / (2 * a)
    root2 = ((-b) - math.sqrt(quad_inside)) / (2 * a)

    if root1 >= 0 and root2 >= 0:
        if root1 > root2:
            return root2
        return root1
    elif root1 >= 0:
        return root1
    elif root2 >= 0:
        return root2
    return None


def find_intersection_point(sphere_list: list, ray: Ray):
    pairs = []
    for i in sphere_list:
        intersect = sphere_intersection_point(ray, i)
        if intersect is not None:
            pairs.append((i, intersect))
    return pairs


def sphere_normal_at_point(spheres: Sphere, points: Point):
    return normalize_Vector(vector_from_to(spheres.center, points))
