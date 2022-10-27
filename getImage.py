import os
import random
import cv2


import pathlib
x = pathlib.Path(__file__).parent.resolve()
print(x)
loc = str(x) + "\\" + "Images2"
subfolders = [ (f.path,f.name) for f in os.scandir(loc) if f.is_dir() ]


while True:
    movie = subfolders[random.randint(0,len(subfolders)-1)]
    # print(movie[1])
    choices = [(f.path,f.name) for f in os.scandir(movie[0]) if f.is_dir()]
    print(choices[0][1])
    # choices
    imageLink = [(f.path,f.name) for f in os.scandir(choices[0][0])]
    # print(imageLink[0][1])
    image = cv2.imread(imageLink[0][0])
    cv2.imshow("Mystery Pokemon",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
