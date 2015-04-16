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
paso=4
umbral=0.38 # para promedios
umbral2=120 # para identificar circulos

while (h1<h-ch):
    while (w1<w-cw):
        if ima2[h1,w1] == 255:
            c+=1
            votos=dict()
            visitados=[]
            visitados2=[]
            j=0
            aux=0
            visitados, n=bfs(ima2,h1,w1)
            Bbox,Bmx,Bmy =box(visitados)
            visitados2, Area_Pixeles=bfs(ima2,Bmy,Bmx)
            pr=round(float(Area_Pixeles)/float(w*h)*100,2)
            votos[(Bmy,Bmx)]=1
            B, G, R=color(c+70)
            mbox=min(Bbox)
            
            while j+paso<len(visitados):
                i1=visitados[j+paso]
                i2=visitados[j]
                angulo1=ang[i1]
                angulo2=ang[i2]
                pt1=[]
                pt2=[]
                pt1=line(h,w,i1[0],i1[1],angulo1+90)
                pt2=line(h,w,i2[0],i2[1],angulo2+90)
                
                x1,x2,x4,x3=max(pt1)[1],min(pt1)[1],max(pt2)[1],min(pt2)[1]
                y1,y2,y4,y3=max(pt1)[0],min(pt1)[0],max(pt2)[0],min(pt2)[0]
                
                den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
                if den!=0:
                    numx = (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)
                    numy = (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)
                    T=(numy/den,numx/den)
                    if T[0] >= 1 and T[0]< h-1 and T[1] >= 1 and T[1] < w-1:
                        My=int(round(float(i2[0]+i1[0])/2))
                        Mx=int(round(float(i2[1]+i1[1])/2))
                        M=(My,Mx)
                        #if M not in visitados2:
                        X1,X2,Y1,Y2=M[1],T[1],M[0],T[0]
                        if X2-X1==0:
                            th=3.1416/2
                        elif Y2-Y1==0:
                            th=0
                        else:
                            pendiente=float(Y2-Y1)/float(X2-X1)
                            th=int(math.degrees(math.atan2(Y2-Y1,X2-X1)))
                        Lines = line(h,w,T[0],T[1],th)
                        for i in Lines:
                            if i not in votos:
                                votos[i]=1
                            else:
                                votos[i]+=1
                j+=paso
            while aux==0:
                v=list(votos.values())
                k=list(votos.keys())
                a=v.index(max(v))
                center=k[a]
                if center not in visitados2:
                    del votos[center]
                else:
                    aux=1
            
            dist=[]
            for i in visitados2:
                out[i]=[B,G,R]
            for i in visitados:
                d=int(math.sqrt((Bmy-i[0])**2+(Bmx-i[1])**2))
                dist.append(d)
            for a in range(-4,5):
                for b in range(-4,5):
                    out[(center[0]+a,center[1]+b)]=[0,0,255]
            for angulo in xrange(0,720):
                if angulo<360:
                    a=max(dist)
                    b=min(dist)
                elif angulo>360:
                    a=max(dist)+1
                    b=min(dist)+1
                y=int(round(center[0]+b*math.sin(math.radians(angulo))))
                x=int(round(center[1]-a*math.cos(math.radians(angulo))))
                out[y,x]=[0,0,255]
            
            cv2.putText(out,"e %d: X^2/%d + Y^2/%d+ = 1" %(c,max(dist),min(dist)), (center[1]-10,center[0]-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (255,0,0))
                    
                    
            
        
                
        w1=w1+1
    w1=0
    h1=h1+1


print "%d elipses detectadas" %c
cv2.imshow('Circle detection',out)
cv2.imwrite('Output.jpg',out)
cv2.imwrite('Input.jpg',ima2)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()



