#A color is generated through the linear congruential method,
#whose input values are the initial value of the sequence
import cv2
import numpy as np
def color(xo):
    B=(4*xo+60)%255
    G=(4*B+20)%255
    R=(4*G+100)%255
    return B,G,R


