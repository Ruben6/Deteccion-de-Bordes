from Subru import *
import cv2

img=cv2.imread('original.jpg',1)
img2=cv2.imread('original.jpg',1)

med=fAvg(img2)

Out=img-med

cv2.imshow('Out',Out)
cv2.imwrite('out.png',Out)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
