from SubAct2 import *
import numpy as np
import cv2



size = (w, h, channels) = (400, 400, 3)
ima2 = np.zeros(size, np.uint8)

ejes(ima2,4)
lines(10,0,12,0, ima2)
lines(20,0,1,25, ima2)
box(-40,-40,40,40,ima2)
circle(200,-80,30,ima2)
ellipse(-80,120,60,20,ima2)


cv2.imshow('Output.jpg',ima2)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()



