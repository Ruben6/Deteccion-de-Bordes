from beproT1 import *          #Edge Detection
from bordesT1 import *         #Edge Detection
from SubrutinasT2 import *   #Shape Detection
from SubrutinasT6 import *
import math

#Read RGB image
img=cv2.imread('original.png',1)
out=cv2.imread('original.png',1)
#gray scale.
img2=gris2(img)
#gaus filter.
img3=gauss(img2)
nimg=gauss(img2)
h,w=nimg.shape
datos=[]
for h1 in xrange(0,h):
    for w1 in xrange(0,w):
        datos.append()
        print nimg[h1,w1]
    
cv2.imshow('shape detection',nimg)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()






cv2.imshow('shape detection',out)
cv2.imwrite('Output.jpg',out)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()



