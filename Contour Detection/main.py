import cv2
import numpy
import os

imagePath = "Contour Detection\contourImage.webp"

if os.path.exists(imagePath):
    image = cv2.imread(imagePath)
    imageGrey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imageGrey, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    count = contours[3] # put -1 for all contours
    cv2.drawContours(image,[count],-1,(0,0,255),3)
    cv2.imshow('Contours', image)

else:
    print("There is no file that matches the path")

cv2.waitKey(0)
cv2.destroyAllWindows
