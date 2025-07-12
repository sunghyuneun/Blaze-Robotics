import numpy
import cv2

def get_limits(colour):

    c = numpy.uint8([[colour]])
    #this is the bgr value to convert to hsv
    hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 5, 100, 100
    upperLimit = hsvC[0][0][0] + 5, 255, 255

    lowerLimit = numpy.array(lowerLimit, dtype = numpy.uint8)
    upperLimit = numpy.array(upperLimit, dtype = numpy.uint8)

    return lowerLimit, upperLimit

