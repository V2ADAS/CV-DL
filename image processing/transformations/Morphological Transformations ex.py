import cv2
import numpy as np

img = cv2.imread('j.png',1) #1 mean no change & 0 gray scale
kernel = np.ones((5,5),np.uint8)


####################### Erosion ################################

erosion = cv2.erode(img,kernel,iterations = 5)


####################### Dilation ################################


dilation = cv2.dilate(img,kernel,iterations = 5)


####################### Opening #################################

img1 = cv2.imread('j1.png',1)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)

####################### closing #################################

img2 = cv2.imread('j2.png',1)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

################# Morphological Gradient#########################

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

##################### Top Hat ###################################

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

##################### Black Hat ###################################

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

##cv2.imshow('j',img)
##cv2.imshow('erosion',erosion)
##cv2.imshow('dilation',dilation)
##cv2.imshow('j*',img1)
##cv2.imshow('opening',opening)
##cv2.imshow('j**',img2)
##cv2.imshow('closing',closing)
##cv2.imshow('gradient',gradient)
cv2.imshow('Top hat',tophat)
cv2.imshow('Black hat',blackhat)

