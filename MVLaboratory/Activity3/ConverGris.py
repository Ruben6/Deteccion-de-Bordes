from SubRu import *
import cv2

img=cv2.imread('original2.jpg',1)
out=cv2.imread('original2.jpg',1)

output1=gray(img)
cv2.imwrite('Output1\Output12.jpg',output1)

output21=cpalette(out,output1,[(255,0,0),(0,255,0),(0,0,255),(55,100,200)])
cv2.imwrite('Output2\Output23.jpg',output21)
output22=cpalette(out,output1,[(255,0,0),(0,255,0),(0,0,255),(55,100,200),(100,200,10),(100,200,0)])
cv2.imwrite('Output2\Output24.jpg',output22)
output23=cpalette(out,output1,[(255,0,0),(0,255,0),(0,0,255),(55,100,200),(100,200,10),(100,200,0),(255,0,200)])
cv2.imwrite('Output2\Output25.jpg',output23)


output31=bin(output1,100)
cv2.imwrite('Output3\Output32.jpg',output31)

            
