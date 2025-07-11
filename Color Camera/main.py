import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255] #yellow in RGB
blue = [255, 0, 0]
green = [0, 255, 0]
red = [0, 0, 255]
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

    greenLowerLimit, greenUpperLimit = get_limits(colour = green)
    greenMask = cv2.inRange(hsvImage, greenLowerLimit, greenUpperLimit)
    greenMaskPil = Image.fromarray(greenMask)
    greenBbox = greenMaskPil.getbbox()
    if greenBbox is not None:
        x1,y1,x2,y2 = greenBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 0), 5)
    
    redLowerLimit, redUpperLimit = get_limits(colour = red)
    redMask = cv2.inRange(hsvImage, redLowerLimit, redUpperLimit)
    redMaskPil = Image.fromarray(redMask)
    redBbox = redMaskPil.getbbox()
    if redBbox is not None:
        x1,y1,x2,y2 = redBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 0, 255), 5)

    yellowLowerLimit, yellowUpperLimit = get_limits(colour = yellow)
    yellowMask = cv2.inRange(hsvImage, yellowLowerLimit, yellowUpperLimit)
    yellowMaskPil = Image.fromarray(yellowMask)
    yellowBbox = yellowMaskPil.getbbox()
    if yellowBbox is not None:
        x1,y1,x2,y2 = yellowBbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 255), 5)
    
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()