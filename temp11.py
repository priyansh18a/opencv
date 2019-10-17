import cv2
import numpy as np
imgpath =  "Downloads\\Compressed\\misc\\misc\\5.1.12.tiff"
#imgpath1 = imgpath + "4.2.01.tiff"
cap = cv2.VideoCapture(0)
ret,img = cap.read()
block = 2
constant = 2
max_value = 255
img1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,block, constant)
#ret, img2 = cv2.threshold(img, th , max_value,cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)
cv2.imshow('frame', img)
cv2.imshow('frame2', img1)
#cv2.imshow('frame3', img2)

 
cap.release()
cv2.destroyAllWindows()