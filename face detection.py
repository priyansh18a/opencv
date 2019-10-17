import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def preprocess(action_frame):

    blur = cv2.GaussianBlur(action_frame, (3,3), 0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_RGB2HSV)

    lower_color = np.array([108, 23, 82])
    upper_color = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    blur = cv2.medianBlur(mask, 5)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
    hsv_d = cv2.dilate(blur, kernel)

    return hsv_d
while True:
    ret,frame = cap.read()
   # img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#    low = np.array([0,10,60])
 #   high = np.array([20,150,255])
 #   mask =  cv2.inRange(img,low,high)
    final = cv2.bitwise_and(frame,frame,mask= preprocess(frame))
    cv2.imshow('frame2',final)
    cv2.imshow('frame1',frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()