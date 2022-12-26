from data import *
from collisions import *
from vector_math import *


def cast_ray(ray: Ray, sphere_list, ambients: Color, light: Light, eye: Point):
    pairs = []

    for p in find_intersection_point(sphere_list, ray):
        pairs.append(p)

    # iterates through found intersections to find the closest sphere
    if len(pairs) > 0:
        index = 0
        min = length_vector(difference_point(ray.pt, pairs[0][1]))

        for item in pairs:
            if length_vector(difference_point(ray.pt, item[1])) < min:
                min = length_vector(difference_point(ray.pt, item[1]))
                index = pairs.index(item)

        closest_sphere = pairs[index][0]
        closest_intersection = pairs[index][1]

        #
        basicColor = Color(ambients.r * closest_sphere.color.r * closest_sphere.finish.ambient,
                           ambients.g * closest_sphere.color.g * closest_sphere.finish.ambient,
                           ambients.b * closest_sphere.color.b * closest_sphere.finish.ambient)

        normalized_intersection = sphere_normal_at_point(closest_sphere, closest_intersection)  # point p's normal, N
        closest_intersection = translate_point(closest_intersection, scale_vector(normalized_intersection, .01))  # pe

        normalized_sphere_light = normalize_Vector(vector_from_to(closest_intersection, light.pt))  # ldir
        dot_product = dot_vector(normalized_sphere_light, normalized_intersection)  # ldotn

        # just added functions
        reflection_vector = difference_vector(normalized_sphere_light, scale_vector(normalized_intersection,
                                                                                    2 * dot_product))  # ldir - 2*ldotn*N
        view_direction = normalize_Vector(vector_from_to(eye, closest_intersection))  # vdir
        specular_intensity = dot_vector(reflection_vector, view_direction)  # vdir * (ldir - 2*ldotn*N )

        diffuse_scale = dot_product * closest_sphere.finish.diffuse
        specularColor = Color(0, 0, 0)
        diffusecolor = Color(0, 0, 0)

        if specular_intensity > 0:  # specular contribution
            specularColor = Color(
                light.color.r * closest_sphere.finish.specular * (
                        specular_intensity ** (1 / closest_sphere.finish.roughness)),
                light.color.g * closest_sphere.finish.specular * (
                        specular_intensity ** (1 / closest_sphere.finish.roughness)),
                light.color.b * closest_sphere.finish.specular * (
                        specular_intensity ** (1 / closest_sphere.finish.roughness))
            )

        if dot_product > 0 and len(
                find_intersection_point(sphere_list, Ray(closest_intersection, normalized_sphere_light))) == 0:
            diffusecolor = Color(
                light.color.r * closest_sphere.color.r * diffuse_scale,
                light.color.g * closest_sphere.color.g * diffuse_scale,
                light.color.b * closest_sphere.color.b * diffuse_scale
            )

        basicColor.r = basicColor.r + diffusecolor.r + specularColor.r
        basicColor.g = basicColor.g + diffusecolor.g + specularColor.g
        basicColor.b = basicColor.b + diffusecolor.b + specularColor.b

        if basicColor.r > 1:
            basicColor.r = 1
        if basicColor.g > 1:
            basicColor.g = 1
        if basicColor.b > 1:
            basicColor.b = 1
        return basicColor

    return Color(1, 1, 1)  # no intersection


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,
                  ambient: Color, light: Light, outfile):
    points = []

    step_x = abs(max_x - min_x) / width
    step_y = abs(max_y - min_y) / height

    try:
        image = open(outfile, "w")
    except FileNotFoundError:
        print("File not Found")

    for i in range(int(height)):
        for j in range(int(width)):
            points.append(Point(min_x + j * step_x, max_y - i * step_y, 0))

    image.write('P3 \n')
    image.write('%d %d \n' % (width, height))
    image.write('255\n')

    for p in points:
        lines = []
        eye_ray = Ray(eye_point, vector_from_to(eye_point, p))
        sphere_color = cast_ray(eye_ray, sphere_list, ambient, light, eye_point)
        lines.append(str(round(255 * sphere_color.r)) + " " + str(round(255 * sphere_color.g)) + " " + str(
            round(255 * sphere_color.b)) + "\n")
        image.writelines(lines)
