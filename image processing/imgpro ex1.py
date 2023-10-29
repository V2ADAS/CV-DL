import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    

    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    
    # Threshold the HSV image to get only blue colors
   # mask = cv2.inRange(hsv, lower_blue, upper_blue)

    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)
    blue_objects = cv2.bitwise_and(frame,frame, mask=blue_mask)
    green_objects = cv2.bitwise_and(frame,frame, mask=green_mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',blue_mask)
    cv2.imshow('mask2',green_mask)
    cv2.imshow('b',blue_objects)
    cv2.imshow('g',green_objects)

    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:

        break
cv2.destroyAllWindows()

