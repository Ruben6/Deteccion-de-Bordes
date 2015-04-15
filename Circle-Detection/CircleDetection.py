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
c=0
paso=2
umbral=0.38 # para promedios
umbral2=120 # para identificar circulos
while (h1<h-ch):
    while (w1<w-cw):
        if ima2[h1,w1] == 255:
            votos=dict()
            visitados=[]
            visitados2=[]
            pt=[]
            j=0
            visitados, n=bfs(ima2,h1,w1)
            Bbox,Bmx,Bmy =box(visitados)
            visitados2, Area_Pixeles=bfs(ima2,Bmy,Bmx)
            pr=round(float(Area_Pixeles)/float(w*h)*100,2)
            votos[(Bmy,Bmx)]=1
            B, G, R=color(c+70)
            angulos=dict()
            for i in visitados:
                angulo=ang[i]
                if angulo not in angulos:
                    angulos[angulo]=1
                else:
                    angulos[angulo]+=1
            k2=list(angulos.keys())

            if len(k2)>umbral2:
                if pr>=umbral:
                    while j<len(visitados):
                        i=visitados[j]
                        angulo=int(ang[i])
                        if angulo==360:
                            angulo=0
            
                        pt = line(h,w,i[0],i[1],angulo)
                        for i in pt:
                            if i not in votos:
                                votos[i]=1
                            else:
                                votos[i]+=1
                        j+=paso
                    v=list(votos.values())
                    k=list(votos.keys())
                    a=v.index(max(v))
                    center=k[a]
                
                    for i in visitados2:
                        out[i]=[B,G,R]

                    for a in range(-4,5):
                        for b in range(-4,5):
                             out[(center[0]+a,center[1]+b)]=[0,0,255]
                         
                    radio=int(round(math.sqrt(Area_Pixeles/float(3.1416))))
                    A=-2*center[1]
                    B=-2*center[0]
                    C=int((center[0])**2 +(center[1])**2-(radio)**2)
                    c+=1
                    for angulo in xrange(0,720):
                        if angulo<360:
                            r=radio
                        elif angulo>360:
                            r=radio+1
                        y=int(round(center[0]+r*math.sin(math.radians(angulo))))
                        x=int(round(center[1]-r*math.cos(math.radians(angulo))))
                        out[y,x]=[0,0,255]
                    cv2.putText(out,"C %d: X^2+Y^2+ %dX+%dY+%d" %(c,A,B,C), (center[1]-10,center[0]-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (255,0,0))
                    
                else:
                    for i in visitados2+visitados:
                        out[i]=[0,0,0]
                    cv2.putText(out,"N/A", (Bmx+4,Bmy-4), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,255))
            else:
                for i in visitados2+visitados:
                    out[i]=[0,0,0]    
        
                
        w1=w1+1
    w1=0
    h1=h1+1


print "%d circulos detectados" %c
cv2.imshow('Circle detection',out)
cv2.imwrite('Output.jpg',out)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()



