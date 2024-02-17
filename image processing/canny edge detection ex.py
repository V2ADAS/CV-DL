import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
   pass

img = cv2.imread('messi5.jpg')

####################################Image Pyramids#######################
lower_reso = cv2.pyrDown(img)
lower_reso2 = cv2.pyrDown(lower_reso)
lower_reso3 = cv2.pyrDown(lower_reso2)

higher_reso2 = cv2.pyrUp(lower_reso3)


##################################canny edge detection####################
edges = cv2.Canny(img,100,200)
edges2 = cv2.Canny(lower_reso,100,200)
edges3 = cv2.Canny(lower_reso2,100,200)
edges4 = cv2.Canny(lower_reso3,100,200)
edges5 = cv2.Canny(higher_reso2,100,200)

cv2.imshow('edges',edges)
cv2.imshow('edges1',edges2)
cv2.imshow('edges2',edges3)
cv2.imshow('edges3',edges4)
cv2.imshow('edges4',edges5)


#######################canny edge detection using trackbars ####################

cv2.namedWindow('trackbars controller')

cv2.createTrackbar('minVal','trackbars controller',0,255,nothing)
cv2.createTrackbar('maxVal','trackbars controller',256,900,nothing)


while(1):
        
    k = cv2.waitKey(1) & 0xFF

    X = cv2.getTrackbarPos('minVal','trackbars controller')
    Y = cv2.getTrackbarPos('maxVal','trackbars controller')      
    edges = cv2.Canny(img,X,Y)
    cv2.imshow('edges',edges)
    if k==27:
        break
cv2.destroyWindow()    

#######################################display images############################


cv2.imshow('image',lower_reso)
cv2.imshow('image2',lower_reso2)
cv2.imshow('image3',lower_reso3)
cv2.imshow('img',higher_reso2)
