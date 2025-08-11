import cv2
import numpy
from PIL import Image
from util import get_limits


yellow = [0, 255, 255] #yellow in RGB
blue = [255, 0, 0]
greenLowerLimit = numpy.array([25, 52, 72], dtype=numpy.uint8)
greenUpperLimit = numpy.array([102, 255, 255], dtype=numpy.uint8)
redLowerLimit1 = numpy.array([0, 100, 100], dtype=numpy.uint8)
redUpperLimit1 = numpy.array([10, 255, 255], dtype=numpy.uint8)
redLowerLimit2 = numpy.array([160, 100, 100], dtype=numpy.uint8)
redUpperLimit2 = numpy.array([179, 255, 255], dtype=numpy.uint8)

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    greenMask = cv2.inRange(hsvImage, greenLowerLimit, greenUpperLimit)
    greenMaskPil = Image.fromarray(greenMask)
    greenBbox = greenMaskPil.getbbox()
    if greenBbox is not None:
        x1,y1,x2,y2 = greenBbox
        #cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 0), 5)
        #cv2.putText(frame, 'GREEN OBJECT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2,cv2.LINE_AA,False)

    greyImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    ret, thresh = cv2.threshold(greyImage, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        cv2.drawContours(frame,[c],-1,(0,0,0),3)
    
    '''
    greyImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    ret, thresh = cv2.threshold(greyImage, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        cv2.drawContours(frame,[c],-1,(0,0,0),3)
    '''


    cv2.imshow('Frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()

