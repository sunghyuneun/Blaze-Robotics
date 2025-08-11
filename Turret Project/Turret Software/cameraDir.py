import cv2
import numpy
from PIL import Image

def aimer(frame):

    redHmax = 10
    redHmin = 160
    redSmin = 200
    redVmin = 100
    centerX = 0

    redLowerLimit1 = numpy.array([0, redSmin, redVmin], dtype=numpy.uint8)
    redUpperLimit1 = numpy.array([redHmax, 255, 255], dtype=numpy.uint8)
    redLowerLimit2 = numpy.array([redHmin, redSmin, redVmin], dtype=numpy.uint8)
    redUpperLimit2 = numpy.array([179, 255, 255], dtype=numpy.uint8)

    kernel = numpy.ones((9,9), numpy.uint8)

    width = 848
    frame = cv2.resize(frame, (width, 480))
    #width = frame.get(cv2.CAP_PROP_FRAME_WIDTH)


    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    redMask = cv2.inRange(hsvImage, redLowerLimit1, redUpperLimit1) + cv2.inRange(hsvImage, redLowerLimit2, redUpperLimit2)
    

    cleanRedMask = cv2.morphologyEx(redMask, cv2.MORPH_CLOSE, kernel)
    cleanRedMask = cv2.morphologyEx(redMask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(cleanRedMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    redMaskPil = Image.fromarray(cleanRedMask)
    redBbox = redMaskPil.getbbox()
    if redBbox is not None:
        x1,y1,x2,y2 = redBbox
        #cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 0, 255), 5)
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                cv2.drawContours(frame,[cnt],-1, (0, 255, 0), 2)
                mome = cv2.moments(cnt)
                if mome["m00"] != 0:
                    centerX = int(mome["m10"] / mome["m00"])
                    centerY = int(mome["m01"]/mome["m00"])
                    cv2.circle(frame,(centerX,centerY),10,(255,0,0),-1)
                else:
                    centerX = -1

        #centerX = (x1 + x2) / 2
        if centerX == -1:
            cv2.putText(frame, 'none',(320, 320),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
            return -1, frame
        elif centerX < (width * .45):
            cv2.putText(frame, 'TARGET: LEFT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
            return centerX, frame
        elif centerX > (width * .55):
            cv2.putText(frame, 'TARGET: RIGHT',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
            return centerX, frame
        else:
            cv2.putText(frame, 'TARGET: FIRE',(x1,y2+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
            return centerX, frame

    else:
        cv2.putText(frame, 'none',(320, 320),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2,cv2.LINE_AA,False)
        return -1, frame


