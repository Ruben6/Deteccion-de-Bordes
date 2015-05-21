
def addf(im,imag,number_of_frames,framePosition):
    
    imag.append(im)
    if framePosition<=number_of_frames:
        im2=sum(imag)
    else:
        imag.pop(0)
        im2=sum(imag)

    return im2
