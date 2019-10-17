import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,800)
cap.set(4,600)

ret,frame1 = cap.read()
ret,frame2 = cap.read()

while True:
    d = cv2.absdiff(frame1, frame2)
    blur = cv2.GaussianBlur(d, (5,5), 0)
    ret,th = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    
    dilated = cv2.dilate(th, np.ones((4,4),np.uint8), iterations = 3)
  #  img1 , c ,h = cv2.findContours(dilated ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   # cv2.drawContours(frame1, c,  -1,(255,0,0) , 2)
    frame3 = frame1
    cv2.imshow("original",frame2)
    cv2.imshow("origin",dilated)
    if cv2.waitKey(1)==27:
        break
    frame1 = frame2
    ret,frame2 = cap.read()
cv2.destroyAllWindows()
cap.release()