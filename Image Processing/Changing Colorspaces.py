"""
Goal
• In this tutorial, you will learn how to convert images from one color-space to another, like BGR ↔ Gray, BGR
↔HSV etc.
• In addition to that, we will create an application which extracts a colored object in a video
• You will learn following functions : cv2.cvtColor(), cv2.inRange() etc
"""

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
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()


"""
Exercises
1. Try to find a way to extract more than one colored objects, for eg, extract red, blue, green objects simultaneously.
"""

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for red color
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Define the lower and upper bounds for blue color
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue_result = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Define the lower and upper bounds for green color
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green_result = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Combine the results for all three colors
    combined_result = cv2.addWeighted(red_result, 1, blue_result, 1, 0)
    combined_result = cv2.addWeighted(combined_result, 1, green_result, 1, 0)

    cv2.imshow('frame', frame)
    cv2.imshow('Red', red_result)
    cv2.imshow('Blue', blue_result)
    cv2.imshow('Green', green_result)
    cv2.imshow('Combined', combined_result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
