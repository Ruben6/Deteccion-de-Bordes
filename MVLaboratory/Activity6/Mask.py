from Subru import *
import cv2
#Pruebas
img=cv2.imread('original.jpg',1)
img2=cv2.imread('original.jpg',1)
gr=gray(img)
gr2=gray(img2)
cv2.imwrite('input.png',gr)

filmin=fmin(gr,gr2)


img3=cv2.imread('input1.png',1)
gr3=gray(img3)
med=median(gr3)

fgauss=gauss(gr)

img4=cv2.imread('original.png',1)
favg=fAvg(img4)


img5=cv2.imread('original.jpg',1)
gr5=gray(img5)
cv2.imwrite('input.png',gr5)
grad=fgrad(gr5)



cv2.imshow('Out',grad)
cv2.imwrite('out3.png',grad)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
