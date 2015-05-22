from Subru import *
import cv2
#Pruebas
img=cv2.imread('original.jpg',1)
gr=gray(img)
cv2.imwrite('input.png',gr)
magnitud, angulo=prewitt(gr)
print magnitud
print angulo





