import sys
from data import *

# eye: default (0.0, 0.0, -14.0) eye has 3 arguments


def process():
    argv = sys.argv
    i = 2

    eyeView = Vector(0, 0, -14)
    views = [-10, 10, -7.5, 7.5, 512, 384]
    light = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
    ambient = Color(1, 1, 1)

    while i < len(argv):
        try:
            flag = argv[i]
            if flag == "-eye":
                try:
                    eyeView = Vector(float(argv[i + 1]), float(argv[i + 2]), float(argv[i + 3]))
                    i = i + 4
                except ValueError:
                    print("wrong value for eye")
                    i = i + 4
                except IndexError:
                    print("not enough values for eye")
                    i = i + 4
            elif flag == "-view":
                try:
                    min_x = float(argv[i + 1])
                    max_x = float(argv[i + 2])
                    min_y = float(argv[i + 3])
                    max_y = float(argv[i + 4])
                    width = float(argv[i + 5])
                    height = float(argv[i + 6])
                    views = [min_x, max_x, min_y, max_y, width, height]
                    i = i + 7
                except ValueError:
                    print("wrong value for view")
                    i = i + 7
                except IndexError:
                    print("not enough values for view")
                    i = i + 7
            elif flag == "-light":
                try:
                    lightPoint = Point(float(argv[i + 1]), float(argv[i + 2]), float(argv[i + 3]))
                    lightColor = Color(float(argv[i + 4]), float(argv[i + 5]), float(argv[i + 6]))
                    light = Light(lightPoint, lightColor)
                    i = i + 7
                except ValueError:
                    print("wrong value for light")
                    i = i + 7
                except IndexError:
                    print("not enough values for light")
                    i = i + 7
            elif flag == "-ambient":
                try:
                    ambient = Color(float(argv[i + 1]), float(argv[i + 2]), float(argv[i + 3]))
                    i = i + 4
                except ValueError:
                    print("wrong value for ambient")
                    i = i + 4
                except IndexError:
                    print("not enough values for ambient")
                    i = i + 4
        except IndexError:
            print("Index error")

    return eyeView, views, light, ambient


"""


def sortParams(argv):
    for i in range(len(argv)):
        flag = argv[i]
        if flag == "-eye":
            try:
                x = argv[i + 1]
                y = argv[i + 2]
                z = argv[i + 3]
                eyeView = Vector(x, y, z)
            except ValueError:
                print("Missing an argument for eye")
                exit()
        else:
            eyeView = Vector(0, 0, -14)

        if flag == "-view":
            try:
                min_x = argv[i + 1]
                max_x = argv[i + 2]
                min_y = argv[i + 3]
                max_y = argv[i + 4]
                width = argv[i + 5]
                height = argv[i + 6]
                view = [min_x, max_x, min_y, max_y, width, height]
            except ValueError:
                print("Missing an argument for view")
                exit()
        else:
            views = [-10, 10, -7.5, 7.5, 512, 384]

        if flag == "-light":
            lightPoint = Point(argv[i + 1], argv[i + 2], argv[i + 3])
            lightColor = Color(argv[i + 4], argv[i + 5], argv[i + 6])
            light = Light(lightPoint, lightColor)
        else:
            light = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))

        if flag == "-ambient":
            ambient = Color(argv[i + 1], argv[i + 2], argv[i + 3])
        else:
            ambient = Color(1, 1, 1)

    return eyeView, view, light, ambient
"""