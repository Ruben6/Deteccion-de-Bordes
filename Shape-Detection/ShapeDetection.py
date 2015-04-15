from beproT1 import *          #Edge Detection
from bordesT1 import *         #Edge Detection
from SubrutinasT2 import *   #Shape Detection
import math

#Read RGB image
img=cv2.imread('original.png',1)
out=cv2.imread('original.png',1)
#gray scale.
img2=gris2(img)
#gaus filter.
img3=gauss(img2)
#Gradient is calculated for each pixel.
m, ang, datos, gx, gy=prewitt(img3)
#ima2: binarized image of dimension h, w
ima2=borde(m,50,img3)
#ang:  Matrix of dimension h, w, that
#      has angles of gradient of each pixel

h, w = ima2.shape
h1=0
w1=0
c=1
c2=0
ch,cw=corrige(ima2,h,w)
Obj_detectados=[]
umbral=0.38
while (h1<h-ch):
    while (w1<w-cw):
        if ima2[h1,w1] == 255:
            visitados, n=bfs(ima2,h1,w1)
            Bbox,Bx,By =box(visitados)
            visitados2, n2=bfs(ima2,By,Bx)
            pr=round(float(len(visitados+visitados2))/float(w*h)*100,2)
            Ch,Cw=centroide(visitados+visitados2)
            if pr>=umbral:
                B, G, R=color(c+50)
                pr2=c2+pr
                Obj_detectados.append(("Figura ID %d: %.2f %%" %(c,pr)))
                for i in visitados2+visitados:
                    out[i]=[B,G,R]
                for i in Bbox:
                    for a in [-1,0]:
                        for b in [0,1]:
                            out[(i[0]+a,i[1]+b)]=[0,255,0]
                cv2.putText(out,"ID %d: %.2f %%" %(c,pr), (Cw+4,Ch-4), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0))
                for a in range(-4,4):
                    for b in range(-4,4):
                         out[(Ch+a,Cw+b)]=[0,0,0]
                c+=1
                c2=pr2
            else:
                for i in visitados2+visitados:
                    out[i]=[0,0,0]
                cv2.putText(out,"N/A", (Cw+4,Ch-4), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0))
                
            
        w1=w1+1
    w1=0
    h1=h1+1
visitados=[]
visitados2=[]
Pr_fondo=100-pr2
Obj_detectados.append(("Fondo:     %.2f %%" %Pr_fondo))
for i in Obj_detectados:
    print i
cv2.putText(out,"Fondo: %.2f %%" %Pr_fondo, (4,15), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,255))




cv2.imshow('shape detection',out)
cv2.imwrite('Output.jpg',out)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()



