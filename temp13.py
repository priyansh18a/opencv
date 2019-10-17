import cv2
import matplotlib.pyplot as plt
import numpy as np
#cap = cv2.VideoCapture(0)
imgpath = "Downloads\\Compressed\\misc\\misc\\4.1.08.tiff"
img = cv2.imread(imgpath)
#ret,img = cap.read(0)
#hist, bins = np.histogram(R.ravel(), 256, [0,255])
#red = cv2.calcHist([img], [0], None, [256],[0,255])
#green = cv2.calcHist([img],[1], None, [256],[0,255])
#blue = cv2.calcHist([img], [2], None, [256],[0,255])
R,G, B = cv2.split(img)
output_1 = cv2.equalizeHist(R)
output_2 = cv2.equalizeHist(G)
output_3 = cv2.equalizeHist(B)
output = cv2.merge((output_1, output_2, output_3))
clahe = cv2.createCLAHE()

output2_1 = clahe.apply(R)
output2_2 = clahe.apply(G)
output2_3 = clahe.apply(B)
output2 = cv2.merge((output2_1, output2_2, output2_3))

cv2.imshow('frame2', img)
cv2.imshow('frame', output)
cv2.imshow('frame1', output2)


cv2.waitKey(0)
#cap.release()
cv2.destroyAllWindows()