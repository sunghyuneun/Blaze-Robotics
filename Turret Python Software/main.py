import cv2
import numpy
from PIL import Image

redHmax = 10
redHmin = 160
redSmin = 180
redVmin = 120

redLowerLimit1 = numpy.array([0, redSmin, redVmin], dtype=numpy.uint8)
redUpperLimit1 = numpy.array([redHmax, 255, 255], dtype=numpy.uint8)
redLowerLimit2 = numpy.array([redHmin, redSmin, redVmin], dtype=numpy.uint8)
redUpperLimit2 = numpy.array([179, 255, 255], dtype=numpy.uint8)

cap = cv2.VideoCapture(0)
kernel = numpy.ones((5,5), numpy.uint8)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#width = 640

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    redMask = cv2.inRange(hsvImage, redLowerLimit1, redUpperLimit1) + cv2.inRange(hsvImage, redLowerLimit2, redUpperLimit2)
    
    cleanRedMask = cv2.erode(redMask,kernel)
    cleanRedMask = cv2.morphologyEx(cleanRedMask, cv2.MORPH_OPEN, kernel)
    cleanRedMask = cv2.dilate(cleanRedMask,kernel)
    cleanRedMask = cv2.morphologyEx(cleanRedMask, cv2.MORPH_CLOSE, kernel)
    '''
    cleanRedMask = cv2.dilate(redMask,kernel)
    cleanRedMask = cv2.morphologyEx(cleanRedMask, cv2.MORPH_CLOSE, kernel)
    cleanRedMask = cv2.erode(cleanRedMask,kernel)
    cleanRedMask = cv2.morphologyEx(cleanRedMask, cv2.MORPH_OPEN, kernel)
    '''

    redMaskPil = Image.fromarray(cleanRedMask)
    redBbox = redMaskPil.getbbox()
    if redBbox is not None:
        x1,y1,x2,y2 = redBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 0, 255), 5)
        centerX = (x1 + x2) / 2
        if centerX < (width * .45):
            cv2.putText(frame, 'TARGET: LEFT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
        elif centerX < (width * .55):
            cv2.putText(frame, 'TARGET: READY TO FIRE',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
        else:
            cv2.putText(frame, 'TARGET: RIGHT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
        
    
    cv2.imshow('Frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()

