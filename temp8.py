import cv2
import time

#imgpath =  "..\\Downloads\\Compressed\\misc\\misc\\"
#imgpath1 = imgpath + "4.2.01.tiff"
cap = cv2.VideoCapture(0)
ret, img1 = cap.read()
rows, columns, channels = img1.shape
angle =0
scale =0
while True:
    if angle == 360 :
        angle = 0
    ret, img1 = cap.read()
    if scale <2:
        scale = scale + 0.1
   
    if scale >=2:
        scale = 1
    rota = cv2.getRotationMatrix2D((columns/2, rows/2), angle ,scale )
    print(rota)
    img3 = cv2.warpAffine(img1, rota, (columns, rows))
    cv2.imshow('frame',img3)
    angle = angle +1
    time.sleep(0.01)
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()