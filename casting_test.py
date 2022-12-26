from cast import *

cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, Point(0, 0, -14),
              [Sphere(Point(1, 1, 0), 2, Color(0, 0, 255), Finish(.2, .4, .5, .05)),
               Sphere(Point(.5, 1.5, -3), .5, Color(255, 0, 0), Finish(.4, .4, .5, .05))],
              Color(1, 1, 1), Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5)))
