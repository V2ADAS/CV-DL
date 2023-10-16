"""
Goal
• Learn to draw different geometric shapes with OpenCV
• You will learn these functions : cv2.line(), cv2.circle() , cv2.rectangle(), cv2.ellipse(), cv2.putText() etc.
"""
import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img = cv.line(img,(0,0),(511,511),(255,0,0),5)
# draw a green rectangle at the top-right corner of image.
img = cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
# draw a circle inside the rectangle drawn above.
img = cv.circle(img,(447,63), 63, (0,0,255), -1)
# draws a half ellipse at the center of the image.
img = cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
# draw a small polygon of with four vertices in yellow color.
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv.polylines(img,[pts],True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('Coded image',img)
cv.waitKey(0)
cv.destroyAllWindows()
