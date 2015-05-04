def norm(img):
    h,w=img.shape
    for h1 in xrange(0,h):
        for w1 in xrange(0,w):
            img[h1,w1]=int(float(img[h1,w1])/255)
    return img
    
