##########################################################################
def gray(img):
    h, w, d = img.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            #El promedio es asignado al pixel y se aloja en un canal
            img[h1, w1,0]=sum(img[h1, w1])//3
     #Se tiene una imagen de salida en escala de grises
    imagen=img[:,:,0]
    return imagen
##########################################################################

def cpalette(out,gris,palette):
    h, w= gris.shape
    n=len(palette)
    block=round(255/n)
    rangos=[]
    c=0
    n1=0
    while n1<n:
        cm=c
        if cm+block > 255:
            cM=255
        else:
            cM=cm+block
        rangos.append((int(cm),int(cM)))
        c=cM+1
        n1+=1
        
        
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            for k in xrange(0,len(rangos)):
                if gris[h1, w1]>=rangos[k][0] and gris[h1, w1]<=rangos[k][1]:
                    out[h1, w1]=palette[k]
                
    return out[:,:,:]
##########################################################################

def bin(gris,threshold):
    h, w= gris.shape
    for h1 in xrange(0,h,1):
        for w1 in xrange(0,w,1):
            if gris[h1, w1]>=threshold:
                gris[h1, w1]=255
            else:
                gris[h1, w1]=0
    return gris[:,:]
            
    
                    
                    
            
    
