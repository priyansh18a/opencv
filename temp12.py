import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)
#imgpath = "Downloads//\\Compressed\\misc\\misc\\5.1.12.tiff"
#mg = cv2.imread(imgpath)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret,img = cap.read()

while True:
    ret,img = cap.read()
    k = np.array(([-1,-1,-1],
              [-1,8,-1],
              [-1,-1,-1]), np.float32)

    output = cv2.filter2D(img, -1, k)
    output2 = cv2.boxFilter(img, -1, (5,5))
    output3 = cv2.GaussianBlur(img, (37, 37), 0)
    output4 = cv2.medianBlur(img, 5)
    output5 = cv2.Laplacian(img, -1, ksize = 23, scale =1, delta =0,borderType = cv2.BORDER_DEFAULT)
    edgesx = cv2.Sobel(img, -1, dx = 5 ,dy= 0,ksize =11,  scale =1, delta =0,borderType = cv2.BORDER_DEFAULT)
    edgesy = cv2.Sobel(img, -1, dx = 0 ,dy= 5,ksize =11,  scale =1, delta =0,borderType = cv2.BORDER_DEFAULT)
    output6  = edgesx +edgesy
    output7= cv2.Canny(img,100,200,L2gradient = True)
    cv2.imshow('frame', output)
    cv2.imshow('frame2', img)
    cv2.imshow('frame3', output2)
    cv2.imshow('frame7', output7)
    cv2.imshow('frame4', output6)

    if cv2.waitKey(1) == 27:
        break 

cap.release()
cv2.destroyAllWindows()