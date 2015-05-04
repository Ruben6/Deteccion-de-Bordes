#Draw coordinate plane.
def ejes(ima2,paso):
    h, w, d= ima2.shape
    ima3=ima2[:,:,2]
    xin=int(round(float(w)/2))
    yin=int(round(float(h)/2))
    for i in xrange(0,h,paso):
        ima3[(i,xin)]=255
    for i in xrange(0,w,paso):
        ima3[(yin,i)]=255
        
    
    return

#(xc,yc); coordinate of the center of line.
#slope and intersection are parameters of line equation.
def lines(xc,yc,slope,intersection,ima2):
    import math
    import random
    h, w, d= ima2.shape
    py=int(round(float(h)/2)-yc)    #coordinate change
    px=int(round(float(w)/2)+xc)    
    angulo=math.atan(slope)
    red=int(random.random()*255)
    green=int(random.random()*255)
    blue=int(random.random()*255)
    x=1
    y=1
    r=0
    a=0
    c=0
    while a<2:
        if c==0:
            th=angulo
        else:
            th=angulo-3.1416
        if y >= 1 and y < h-1 and x >= 1 and x < w-1:
            x=int(round(px-r*math.cos(th)+intersection))
            y=int(round(py+r*math.sin(th)))
            r+=1
        else:
            x=1
            y=1
            r=0
            c=1
            a+=1
        ima2[(y,x)]=[blue,green,red]
            
    return
#(xc,yc); coordinate of the center of the box (rectangle or square).
#width,height; are parameters of rectangle or square.
#ima2; original image
def box(xc,yc,width,height,ima2):
    import math
    import random
    red=int(random.random()*255)
    green=int(random.random()*255)
    blue=int(random.random()*255)
    h, w, d= ima2.shape
    py=int(round(float(h)/2)-yc)    #coordinate change
    px=int(round(float(w)/2)+xc)
    mw=px-int(float(width)/2)
    Mw=px+int(float(width)/2)
    mh=py-int(float(height)/2)
    Mh=py+int(float(height)/2)
    
    for i in range(mw, Mw):
        for j in range(mh,Mh):
            if j >= 1 and j < h-1 and i >= 1 and i < w-1:
                ima2[(j,i)]=[blue,green,red]
    return
#A,B ;  parameters of circle equation
#radio; radius circle
#ima2; original image
def circle(A,B,radio,ima2):
    import math
    import random
    h, w, d= ima2.shape
    yc=int(round(-float(B)/2))
    xc=int(round(-float(A)/2))
    py=int(round(float(h)/2)-yc)    #coordinate change
    px=int(round(float(w)/2)+xc)
    #radio=int(round(float(math.sqrt(yc*yc + xc*xc - C))))
    red=int(random.random()*255)
    green=int(random.random()*255)
    blue=int(random.random()*255)
    
    while radio >=0:
        for angulo in xrange(0,360):
            y=int(round(py+radio*math.sin(math.radians(angulo))))
            x=int(round(px-radio*math.cos(math.radians(angulo))))
            if y >= 1 and y < h-1 and x >= 1 and x < w-1:
                ima2[y,x]=[blue,green,red]
        radio-=0.1

#(xc,yc); coordinate of the center of the ellipse.
#(a,b)  ;larger radius and a smaller radius, respectively.
#ima2; original image
def ellipse(xc,yc,a,b,ima2):
    import math
    import random
    ra=0
    rb=0
    h, w, d= ima2.shape
    py=int(round(float(h)/2)-yc)    #coordinate change
    px=int(round(float(w)/2)+xc)
    red=int(random.random()*255)
    green=int(random.random()*255)
    blue=int(random.random()*255)
    while a>=0 and b>=0:
        if ra < a and rb < b:
            for angulo in xrange(0,360):
                y=int(round(py+b*math.sin(math.radians(angulo))))
                x=int(round(px-a*math.cos(math.radians(angulo))))
                if y >= 1 and y < h-1 and x >= 1 and x < w-1:
                    ima2[y,x]=[blue,green,red]
        a-=0.1
        b-=0.1
