
import sys
import commandline
from cast import *


def readFile(argv):
    sphereList = []
    try:
        sphere = open(argv[1], "r")
        linenumber = 0
        for line in sphere:
            linenumber += 1
            datas = line.split()
            center = Point(float(datas[0]), float(datas[1]), float(datas[2]))
            rad = float(datas[3])
            color = Color(float(datas[4]), float(datas[5]), float(datas[6]))
            ambient = float(datas[7])
            diffuse = float(datas[8])
            specular = float(datas[9])
            roughness = float(datas[10])
            finish = Finish(ambient, diffuse, specular, roughness)
            sphere = Sphere(center, rad, color, finish)
            sphereList.append(sphere)
    except IndexError:
        print('skipping malformed sphere with' + str(linenumber))
        exit()
    except ValueError:
        print('skipping malformed sphere with' + str(linenumber))
        exit()
    return sphereList


"""
def createSphere(sphereValue):
    i = 0
    sphere_list = []
    while i < len(sphereValue):
        center = Point(sphereValue[i], sphereValue[i + 1], sphereValue[i + 2])
        rad = sphereValue[i + 3]
        color = Color(sphereValue[i + 4], sphereValue[i + 5], sphereValue[i + 6])
        ambient = sphereValue[i + 7]
        diffuse = sphereValue[i + 8]
        specular = sphereValue[i + 9]
        roughness = sphereValue[i + 10]
        finish = Finish(ambient, diffuse, specular, roughness)
        sphere = Sphere(center, rad, color, finish)
        sphere_list.append(sphere)
        i = i + 12
    return sphere_list
"""


# def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,
#                   ambient: Color, light: Light):
#    return eyeView, view, light, ambient


def main():
    argv = sys.argv
    sphereList = readFile(argv)
    command = commandline.process()
    cast_all_rays(command[1][0], command[1][1], command[1][2], command[1][3], command[1][4],
                  command[1][5], command[0], sphereList, command[3], command[2], "image.ppm")


main()

"""
if __name__ == "__main__":
    main(sys.argv)
"""
