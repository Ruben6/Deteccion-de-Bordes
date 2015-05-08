
from color import *
import numpy as np
import cv2

size = (w, h, channels) = (400, 400, 3)
ima2 = np.zeros(size, np.uint8)
c=1
while c<=3:
    B,G,R =color(c*10)
    for i in xrange(0,h):
        for j in xrange(0,w):
            ima2[(i,j)]=[B,G,R]
    cv2.imwrite('Output %d.jpg' %c,ima2)
    c+=1

