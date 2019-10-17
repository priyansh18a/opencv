import cv2
import numpy as np
imgpath =  "Downloads\\Compressed\\misc\\misc\\5.1.09.tiff"
#imgpath1 = imgpath + "4.2.01.tiff"
img =  cv2.imread(imgpath,0)
th = 0
max_value = 255
ret, img1 = cv2.threshold(img, th , max_value,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, img2 = cv2.threshold(img, th , max_value,cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)
ret, img3 = cv2.threshold(img, th , max_value,cv2.THRESH_TOZERO+ cv2.THRESH_OTSU)
ret, img4 = cv2.threshold(img, th , max_value,cv2.THRESH_TOZERO_INV+ cv2.THRESH_OTSU)
ret, img5 = cv2.threshold(img, th , max_value,cv2.THRESH_TRUNC+ cv2.THRESH_OTSU)
cv2.imshow('frame', img)
cv2.imshow('frame2', img1)
cv2.imshow('frame3', img2)
cv2.imshow('frame4', img3)
cv2.imshow('frame5', img4)
cv2.imshow('frame6', img5)
 
cv2.waitKey(0)
cv2.destroyAllWindows()