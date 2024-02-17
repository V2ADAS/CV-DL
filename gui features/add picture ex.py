import cv2
import numpy as np
##img1 = cv2.imread('messi5.jpg')
##img = cv2.imread('1.jpg')
##y=cv2.add(img,img1)
##cv2.imshow("img",y)
e1 = cv2.getTickCount()


img1 = cv2.imread('ml.PNG')
resized_image = cv2.resize(img1,None,fx=2, fy=2,interpolation=cv2.INTER_AREA)
img2 = cv2.imread('opencv_logo.jpg')
resized_image2 = cv2.resize(img2, None,fx=2, fy=2, interpolation=cv2.INTER_AREA)
dst = cv2.addWeighted(resized_image,0.7,resized_image2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

### Load two images
##img1 = cv2.imread('messi5.jpg')
##img2 = cv2.imread('opencv_logo.png')
### I want to put logo on top-left corner, So I create a ROI
##rows,cols,channels = img2.shape
##roi = img1[0:rows, 0:cols ]
### Now create a mask of logo and create its inverse mask also
##img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
##ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
##mask_inv = cv2.bitwise_not(mask)
### Now black-out the area of logo in ROI
##img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
### Take only region of logo from logo image.
##img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
### Put logo in ROI and modify the main image
##dst = cv2.add(img1_bg,img2_fg)
##img1[0:rows, 0:cols ] = dst
##cv2.imshow('res',img1)
##cv2.imshow('res1',img1_bg)
##cv2.imshow('res2',img2_fg)
##
##e2 = cv2.getTickCount()
##time = (e2 - e1)/ cv2.getTickFrequency()
##print(time)
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()
