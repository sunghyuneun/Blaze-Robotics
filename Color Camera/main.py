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

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blueLowerLimit, blueUpperLimit = get_limits(colour = blue)
    blueMask = cv2.inRange(hsvImage, blueLowerLimit, blueUpperLimit)
    blueMaskPil = Image.fromarray(blueMask)
    blueBbox = blueMaskPil.getbbox()
    if blueBbox is not None:
        x1,y1,x2,y2 = blueBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (255, 0, 0), 5)
        cv2.putText(frame, 'BLUE OBJECT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2,cv2.LINE_AA,False)
        

    greenMask = cv2.inRange(hsvImage, greenLowerLimit, greenUpperLimit)
    greenMaskPil = Image.fromarray(greenMask)
    greenBbox = greenMaskPil.getbbox()
    if greenBbox is not None:
        x1,y1,x2,y2 = greenBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 0), 5)
        cv2.putText(frame, 'GREEN OBJECT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2,cv2.LINE_AA,False)
    
    redMask = cv2.inRange(hsvImage, redLowerLimit1, redUpperLimit1) + cv2.inRange(hsvImage, redLowerLimit2, redUpperLimit2)
    redMaskPil = Image.fromarray(redMask)
    redBbox = redMaskPil.getbbox()
    if redBbox is not None:
        x1,y1,x2,y2 = redBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 0, 255), 5)
        cv2.putText(frame, 'RED OBJECT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)

    yellowLowerLimit, yellowUpperLimit = get_limits(colour = yellow)
    yellowMask = cv2.inRange(hsvImage, yellowLowerLimit, yellowUpperLimit)
    yellowMaskPil = Image.fromarray(yellowMask)
    yellowBbox = yellowMaskPil.getbbox()
    if yellowBbox is not None:
        x1,y1,x2,y2 = yellowBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 255), 5)
        cv2.putText(frame, 'YELLOW OBJECT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),2,cv2.LINE_AA,False)
    
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()