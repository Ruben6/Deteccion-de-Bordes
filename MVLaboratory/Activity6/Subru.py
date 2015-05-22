# -*- coding: cp1252 -*-
# inicia
def gray(img):
    h, w, d = img.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            #El promedio es asignado al pixel y se aloja en un canal
            img[h1, w1,0]=sum(img[h1, w1])//3
     #Se tiene una imagen de salida en escala de grises
    imagen=img[:,:,0]
    return imagen

####################################################
#Mascaras de ordenamiento.
def median(gray):
    h, w= gray.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            l=[]
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if h1+i>=0 and h1+i<h and w1+j>=0 and w1+j<w:
                        l.append(gray[h1+i,w1+j])
            l.sort()
            if len(l)%2==0:
                med=(l[len(l)/2 -1]+l[len(l)/2])/2
            else:
                med=l[len(l)/2]
            gray[h1,w1]=med
            
                        
    return gray

####################################################
def fmin(gray,gr2):
    h, w= gray.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            l=[]
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if h1+i>=0 and h1+i<h and w1+j>=0 and w1+j<w:
                        l.append(gray[h1+i,w1+j])
            gr2[h1,w1]=min(l)
            
                        
    return gr2

##########################################################################
#Mascaras de convolución.
def gauss(img2):
    h, w = img2.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            #se establece una regla para evitar
            #conflictos con coordenadas fuera del rango
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
            #se aplica el flitro gausiano, que es una mascara de dimencion 3x3
            sum1=1*img2[h1, w1].tolist()+2*img2[h1, w2].tolist()*a+1*img2[h1, w3].tolist()*c
            sum2=2*img2[h2, w1].tolist()*b+4*img2[h2, w2].tolist()*b*a+2*img2[h2, w3].tolist()*b*c
            sum3=1*img2[h3, w1].tolist()*d+2*img2[h3, w2].tolist()*d*a+1*img2[h3, w3].tolist()*d*c
            suma=(1./16)*(sum1+sum3+sum3)
            img2[h1, w1]=suma
    return img2
####################################################
#Mascara AVG.
def fAvg(img):
    h, w, d = img.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            #Regla para evitar el efecto dona
            if w1==0:
                b=0
            else:
                b=1
            if h1==0:
                a=0
            else:
                a=1
            if w1==w-1:
                w2=w1
                d=0
            else:
                w2=w1+1
                d=1

            if h1==h-1:
                h2=h1
                c=0
            else:
                h2=h1+1
                c=1
            #Se realiza la sumatoria de los valores de cada vecino para cada canal RGB
            for i in range(len(img[h1, w1].tolist())):
                sum1=img[h1-1, w1-1].tolist()[i]*a*b+img[h1-1, w1].tolist()[i]*a+img[h1-1, w2].tolist()[i]*a*d
                sum2=img[h1, w1-1].tolist()[i]*b+img[h1, w1].tolist()[i]+img[h1, w2].tolist()[i]*d
                sum3=img[h2, w1-1].tolist()[i]*b*c+img[h2, w1].tolist()[i]*c+img[h2, w2].tolist()[i]*c*d
                #se calcula el promedio
                med=(sum1+sum3+sum3)//(a*b+a+a*d+b+d+b*c+c+c*d+1) 
            #El promedio es asignado al pixel en sus tres canales
            img[h1, w1]=[med,med,med]     
    return img

########################################################
#Mascara de convolucion discreta, gradiente (Prewitt 0°).
def fgrad(img2):
    h, w = img2.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            #se establece una regla para evitar
            #conflictos con coordenadas fuera del rango
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
            #se aplica la mascara Prewitt a 0°
            sum1=-1*img2[h1, w1].tolist()+1*img2[h1, w2].tolist()*a+1*img2[h1, w3].tolist()*c
            sum2=-1*img2[h2, w1].tolist()*b-2*img2[h2, w2].tolist()*b*a+1*img2[h2, w3].tolist()*b*c
            sum3=-1*img2[h3, w1].tolist()*d+1*img2[h3, w2].tolist()*d*a+1*img2[h3, w3].tolist()*d*c
            suma=sum1+sum3+sum3
            img2[h1, w1]=suma
    return img2

