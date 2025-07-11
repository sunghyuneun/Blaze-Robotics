import numpy
import cv2

colour = [0, 255, 255]

c = numpy.uint8([[colour]])
#this is the bgr value to convert to hsv
hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

lowerLimit = hsvC[0][0][0] - 10, 100, 100
upperLimit = hsvC[0][0][0] + 10, 255, 255


print(lowerLimit)
print("\n")
print(upperLimit)