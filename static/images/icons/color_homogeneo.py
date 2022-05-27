# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:09:06 2022

@author: MX03597
"""

import cv2 as cv
import os
import numpy as np

os.chdir('/home/kevin/Documents/Python/SitioWeb/Portafolio/static/images/icons');
objects = os.listdir();
imgSet = [];

for i in objects:
    if i[-3:] == 'png' and not i[0] in ['0','1','2','3','4','5','6','7','8','9',]:
        imgSet.append(cv.imread(i,cv.IMREAD_UNCHANGED))

lenx = imgSet[0].shape[0]
leny = imgSet[0].shape[1]
lenChannel = imgSet[0].shape[2]
c = 0;
for img in imgSet:
    for x in range(lenx):
        for y in range(leny):
            if img[x][y][3] == 255:
                img[x][y][0] = 170;
                img[x][y][1] = 170;
                img[x][y][2] = 170;
    cv.imwrite("blanco/{} blanco.png".format(c),img);
    c += 1;



"""
c = 0;
for i in imgSet:

    print(i.shape[0])
    print(i.shape[1])
    print(i.shape[2])
    print()
    cv.imwrite("{}.png".format(c), i);
    c += 1;
"""


"""
lenx = imgSet[0].shape[0]
leny = imgSet[0].shape[1]
lenChannel = imgSet[0].shape[2]
val = ''

for i in range(lenx):
    for j in range(leny):
        val = val + ' ' + str(imgSet[0][i][j][3])

print(val)
"""
"""
bgr = imgSet[0][:,:,:3] # Channels 0..2
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)

# Some sort of processing...

bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
alpha = imgSet[0][:,:,3] # Channel 3
result = np.dstack([bgr, alpha]) # Add the alpha channel

cv.imwrite('test.png', result)
"""