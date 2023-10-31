import numpy as np
import cv2

im = cv2.imread('box.png')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


# Create a copy of the original image
im_copy = im.copy()
#im_copy2 = im.copy()

img = cv2.drawContours(im_copy, contours, -1, (0,255,0), 3)#-1 to draw all contours
#img2 = cv2.drawContours(im_copy2, contours, 2, (0,255,0), 3)#drawing the 4th contour


cv2.imshow('img1',img)
#cv2.imshow('img2',img2)










