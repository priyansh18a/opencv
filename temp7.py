import cv2
# import matplotlib.pyplot as plt
import numpy as np
import time

imgpath =  "..\\Downloads\\Compressed\\misc\\misc\\"
imgpath1 = imgpath + "4.2.01.tiff"
imgpath2 = imgpath + "4.2.04.tif"

img1 = cv2.imread(imgpath1,1)
img2 = cv2.imread(imgpath2,1)
alpha  = 0
beta = 1
for i in np.linspace(0, 1, 20):
    alpha = i
    beta = 1-i
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    cv2.imshow('frame', output)
    time.sleep(0.2)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()

 