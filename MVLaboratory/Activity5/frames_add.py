import cv2
import numpy as np

cap = cv2.VideoCapture(0)
imag=[]
c=0
fr=int(raw_input("Please enter the number of frames to add:"))
while True:
    if cap.read():
        f, im = cap.read()
        if not f:
            continue
        else:
            imag.append(im)
            if c<=fr:
                im2=sum(imag)
            else:
                imag.pop(0)
                im2=sum(imag)

            cv2.imshow('video', im2)
            c+=1 
    if cv2.waitKey(10) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
   
