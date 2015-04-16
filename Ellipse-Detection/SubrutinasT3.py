#The predominant angle is detected
def Angulo(ang,visitados):
    import math
    gn=dict()
    th=[]
    for i in visitados:
        theta=int(90+ang[i])
        th.append(theta)
        if theta==360:
            theta=0
        if theta not in gn:
            gn[theta]=1
        else:
            gn[theta]+=1
    v=list(gn.values())
    k=list(gn.keys())
    a=v.index(max(v))
    return k[a]

#from the Hough transform, the linear regressor is calculated
#for each line detected
def line(h,w,py,px,angulo):
    import math
    x=1
    y=1
    r=0
    a=0
    b=0
    pt=[]
    while a<2:
        if b==0:
            th=angulo
        else:
            th=angulo-180
        if y >= 1 and y < h-1 and x >= 1 and x < w-1:
            x=int(round(px-r*math.cos(math.radians(th))))
            y=int(round(py+r*math.sin(math.radians(th))))
            r-=1
            pt.append((y,x))
        else:
            x=1
            y=1
            r=0
            b=1
            a+=1
            
    return pt

#The bounding box and additional parameters are calculated
def box2(visitados):
    import math
    h=[]
    w=[]
    box=[]
    for i in visitados:
        h.append(i[0])
        w.append(i[1])
    Mh=max(h)
    mh=min(h)
    Mw=max(w)
    mw=min(w)
    for i in range(mw, Mw):
        box.append((mh,i))
    for i in range(mh,Mh+1):
        box.append((i,Mw))
    for i in range(mh+1,Mh):
        box.append((i,mw))
    for i in range(mw,Mw):
        box.append((Mh,i))
    Bmx=mw+int((Mw-mw)/2)
    Bmy=mh+int((Mh-mh)/2)
    mag=math.sqrt((Mw-mw)**2 + (Mh-mh)**2)
    return box,Bmx,Bmy, mag
