from Subru import *
import cv2

img=cv2.imread('original.jpg',1)
img2=cv2.imread('original.jpg',1)
gr=gray(img)
gr2=gray(img2)
cv2.imwrite('input.png',gr)

filmin=fmin(gr,gr2)


#img3=cv2.imread('input1.png',1)
#gr3=gray(img3)
#med=median(gr3)

fgauss=gauss(gr)




cv2.imshow('shape detection',fgauss)
cv2.imwrite('out2.png',fgauss)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
