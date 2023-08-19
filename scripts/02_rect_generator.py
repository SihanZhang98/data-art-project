import sys
import cv2
import copy
import itertools
from PIL import Image, ImageOps, ImageDraw
from copy import deepcopy
from operator import itemgetter
from statistics import median, mean
from math import sqrt
from random import randint


# generation parameters (CAN CHANGE)
num_pics = 5
num_rect = randint(5, 15)
canvas_width = 20
canvas_height = 20
min_size = 1
max_size = 5
increments = 80

for count in range(num_pics): 

# Basic vision
    visual = Image.open(r'D:\Python\AutoSceenshot\blank.jpg')                      # must feed in blank, black canvas image as input (blank.png)
    draw = ImageDraw.Draw(visual)




# Generate random number of rectangles (must be touching) of random sizes
    boxes = []
    for i in range(num_rect):
        valid = 0
        while(valid == 0):
            width = randint(min_size, max_size)*increments
            height = randint(min_size, max_size)*increments
            pos_x = randint(max_size+1, canvas_width-max_size-1)*increments
            pos_y = randint(max_size+1, canvas_height-max_size-1)*increments
            for j in boxes:
                touching = 1
                if (pos_x+(width/2.0) < j[0]-(j[2]/2.0)):
                    touching = 0
                if (pos_x-(width/2.0) > j[0]+(j[2]/2.0)):
                    touching = 0
                if (pos_y+(height/2.0) < j[1]-(j[3]/2.0)):
                    touching = 0
                if (pos_y-(height/2.0) > j[1]+(j[3]/2.0)):
                    touching = 0
                if touching == 1:
                    valid = 1
            if len(boxes) == 0:
                valid = 1
        boxes.append([pos_x,pos_y,width,height])

    # Draw resulting rectangles as image

    for i in boxes:
        # print(i)
        top_left = (i[0]-(i[2]/2.0),i[1]-(i[3]/2.0))
        bottom_right = (i[0]+(i[2]/2.0),i[1]+(i[3]/2.0))
        draw.rectangle((top_left,bottom_right), fill='white')
        visual.save(f"output{count}.png")

print("finish!")