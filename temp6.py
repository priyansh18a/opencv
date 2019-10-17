import cv2
import numpy as np


cap = cv2.VideoCapture(1)
ret = True
while ret:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low = np.array([140,50,50])
    high = np.array([80,255,255])
    image_mask = cv2.inRange(img, low, high)
    final = cv2.bitwise_and(frame, frame,mask = image_mask)
    
    cv2.imshow('window', frame)
    cv2.imshow('green color', image_mask )
    cv2.imshow('color', final )

    if cv2.waitKey(1) == 27:
        break 

cv2.destroyAllWindows()
cap.release()
 





