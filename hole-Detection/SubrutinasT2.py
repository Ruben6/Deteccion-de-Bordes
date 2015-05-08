#A color is generated through the linear congruential method,
#whose input values are the initial value of the sequence
import cv2
import numpy as np
def color(xo):
    B=(4*xo+10)%255
    G=(4*B+10)%255
    R=(4*G+10)%255
    return B,G,R

#Through a DFS a set of pixels is defined
def bfs(bina,h1,w1):
    h, w = bina.shape
    bandera=254
    n=0
    q=[]
    visitados=[]
    frecuencias=dict()
    q.append((h1,w1))
    original=bina[(h1,w1)]
    while len(q) > 0:
        (h1, w1) = q.pop(0)
        actual = bina[h1, w1]
        if actual == original or actual == bandera:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    i, j = (h1 + dx, w1 + dy)
                    if i >= 0 and i < h and j >= 0 and j < w:
                        contenido = bina[i, j]
                        if contenido == original:
                            bina[i, j]=bandera
                            visitados.append((i,j))
                            n += 1
                            q.append((i, j))
    return visitados, n
#Determines a bounding box
def box(visitados):
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
    return box,Bmx,Bmy

#A correction of an strange object produced in the preprocessing
def corrige(bina,h,w):
    c=0
    cw=1
    ch=1
    while (c==0):
        if bina[0,w-cw]==255:
            cw+=1
        else:
            c=1
    c=0
    while (c==0):
        if bina[h-ch,0]==255:
            ch+=1
        else:
            c=1
    return ch-1,cw-1

#Calculation of the center of mass
def centroide(visitados):
    Ch=[]
    Cw=[]
    for i in visitados:
        Ch.append(i[0])
        Cw.append(i[1])
    Ch=sum(Ch)/len(visitados)
    Cw=sum(Cw)/len(visitados)
    return Ch,Cw



                                         
                                
