
import numpy as np
import math
def gray(img):
    h, w, d = img.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            #El promedio es asignado al pixel y se aloja en un canal
            img[h1, w1,0]=sum(img[h1, w1])//3
     #Se tiene una imagen de salida en escala de grises
    imagen=img[:,:,0]
    return imagen

def prewitt(img2):
    h, w = img2.shape
    m=np.empty((h, w))
    ang=np.empty((h,w))

    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            #se establece una regla para evitar conflictos
            #con coordenadas fuera del rango
            if w1==w-1:
                w2=w1
                a=0
            else:
                w2=w1+1
                a=1
            if h1==h-1:
                h2=h1
                b=0
            else:
                h2=h1+1
                b=1
            if w1>=w-2:
                w3=w1
                c=0
            else:
                w3=w1+2
                c=1
            if h1>=h-2:
                h3=h1
                d=0
            else:
                h3=h1+2
                d=1
            # se aplica la mascara de deteccion de borde Prewitt paea la commponente
            #horizontal
            con1x=-1*img2[h1, w1].tolist()+0*img2[h1, w2].tolist()*a+1*img2[h1, w3].tolist()*c
            con2x=-1*img2[h2, w1].tolist()*b+0*img2[h2, w2].tolist()*b*a+1*img2[h2, w3].tolist()*b*c
            con3x=-1*img2[h3, w1].tolist()*d+0*img2[h3, w2].tolist()*d*a+1*img2[h3, w3].tolist()*d*c
            convx=con1x+con2x+con3x
            # se aplica la mascara de deteccion de borde Prewitt paea la commponente
            #vertical
            con1y=1*img2[h1, w1].tolist()+1*img2[h1, w2].tolist()*a+1*img2[h1, w3].tolist()*c
            con2y=0*img2[h2, w1].tolist()*b+0*img2[h2, w2].tolist()*b*a+0*img2[h2, w3].tolist()*b*c
            con3y=-1*img2[h3, w1].tolist()*d-1*img2[h3, w2].tolist()*d*a-1*img2[h3, w3].tolist()*d*c
            convy=con1y+con2y+con3y
            if convx > 0 and convy == 0:
                theta = 0
            elif convx < 0 and convy == 0:
                theta = 180
            if convx == 0 and convy > 0:
                theta = 90
            elif convx == 0 and convy < 0:
                theta = 270
            else:
                theta = int(math.degrees(math.atan2(convy,convx)))
            #para reducir coste, se obtiene la magnitud del gradiente
            #a travez de una aproximacion.
            g=abs(convx)+abs(convy)
            #Se asignan los valores de la magnitud a la matriz m
            m[h1,w1]=g
            ang[h1,w1]=theta

    return m, ang
#####################################################################
