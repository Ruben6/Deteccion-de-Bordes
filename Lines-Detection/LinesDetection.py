from beproT1 import *          #Edge Detection
from bordesT1 import *         #Edge Detection
from SubrutinasT2 import *     #Shape Detection
from SubrutinasT3 import *     #Line Detection
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
ch,cw=corrige(ima2,h,w)
colores=dict()
c=0
lista_de_angulos=[]
lista_de_colores=[]

while (h1<h-ch):
    while (w1<w-cw):
        if ima2[h1,w1] == 255:
            visitados, n=bfs(ima2,h1,w1)
            Bbox,Bx,By,mag =box2(visitados)
            angulo=Angulo(ang,visitados)
            pt = line(h,w,By,Bx,angulo)
            B, G, R=color(c+70)
            if angulo not in lista_de_angulos:
                lista_de_angulos.append(angulo)
                lista_de_colores.append([B,G,R])
            
            color_asignado=lista_de_colores[lista_de_angulos.index(angulo)]

            for i in visitados:
                out[i]=color_asignado
            
            for i in pt:
                out[i]=[0,0,255]
                
            for a in range(-4,5):
                    for b in range(-4,5):
                         out[(By+a,Bx+b)]=[0,0,255]
                         
            if angulo !=0 and angulo !=180 and angulo !=90 and angulo !=270:
                m=-1*float(math.cos(angulo))/float(math.sin(angulo))
                b=mag/float(math.sin(angulo))
                if b>0:
                    sig="+"
                else:
                    sig="-"
                cv2.putText(out,"Angulo %d; y=%.2fx%s%.2f" %(angulo,m,sig,abs(b)), (Bx+4,By-4), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,0,0))
            else:
                cv2.putText(out,"Angulo %d; N/A" %(angulo), (Bx+4,By-4), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,0,0))

            c+=1
        w1=w1+1
    w1=0
    h1=h1+1




cv2.imshow('Bordes Prewitt',out)
cv2.imwrite('Input.jpg',ima2)
cv2.imwrite('Output.jpg',out)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()



