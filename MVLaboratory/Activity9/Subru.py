

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
