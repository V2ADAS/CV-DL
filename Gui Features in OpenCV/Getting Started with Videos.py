"""
Goal
• Learn to read video, display video and save video.
• Learn to capture from Camera and display it.
• You will learn these functions : cv2.VideoCapture(), cv2.VideoWriter()
"""
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

## Playing Video from file
cap = cv.VideoCapture('videoplayback.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

## Saving a Video

cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
# Check the frame rate and resolution
fps = cap.get(cv.CAP_PROP_FPS)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, fps, (width,height))  # 20 is frame rate & (640,480) is resolution
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # frame = cv.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()