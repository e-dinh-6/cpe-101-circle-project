# cpe-101-circle-project

This was a month long project in which using an array and two circles, you are able to change the size of the circle through the command line printing 
it to a file. The array is used as a light source and the smaller circle is the area where the light hits. 

The image below is the what is outputted after typing in the following command line arguments: 
py ray_caster.py sphere.in -light -150 50 -100 1.5 1.5 1.5

![image](https://user-images.githubusercontent.com/66757056/209517531-465a23ae-b292-4eee-be54-3dbc97ad1bfb.png)

The position of the sphere can be shifted: 

py ray_caster.py sphere.in -light -150 50 -100 1.5 1.5 1.5 -view -5 15 -5 10 512 384
![Screenshot_20230122_083539](https://user-images.githubusercontent.com/66757056/213968218-eb96181a-67f7-4b1d-bbed-8b03e94fcc10.png)


Changing the sphere input to smaller sphere varying in different sizes, bunny.in, this can be used to create an image of a bunny. 
py ray_caster.py bunny.in

![Screenshot_20230119_102429](https://user-images.githubusercontent.com/66757056/213968153-12413ca4-a68c-4102-ba9f-2b1bc9d706bc.png)
