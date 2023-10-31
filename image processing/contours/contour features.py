import cv2
import numpy as np

img = cv2.imread('star.PNG',0)
im_copy = img.copy()

img2 = cv2.imread('spark.PNG',0)

img2 = 255 - img2
img_copy = img2.copy()

ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

ret2,thresh2 = cv2.threshold(img2,127,255,0)
contours2,hierarchy2 = cv2.findContours(thresh2, 1, 2)

#################### moment #############################

cnt = contours[0]
cnt2 = contours2[0]
M = cv2.moments(cnt)

#################### centroid ###########################
##
##cx = int(M['m10']/M['m00'])
##cy = int(M['m01']/M['m00'])
##
########################### AREA ############################
##
##area = cv2.contourArea(cnt)
##
##perimeter = cv2.arcLength(cnt,True)
##
########################## Contour Approximation ############
##
##epsilon = 0.001*perimeter
##
##approx = cv2.approxPolyDP(cnt,epsilon,True )
##
### Display the converted image
##
##cv2.drawContours(im_copy, [approx], -1, (80, 0, 0), 3)
##
##cv2.imshow('Approximated Contour', im_copy)
##
#######################  convex hull  ########################
##
##hull = cv2.convexHull(cnt)
##
##im2_copy = img.copy()
##
##cv2.drawContours(im2_copy, [hull], -1, (80, 0, 0), 3)
##
##cv2.imshow('convex hull Contour', im2_copy)

#######################  RECTANGLE  ##########################


##x,y,w,h = cv2.boundingRect(cnt2)
##img_copy = cv2.rectangle(img_copy,(x,y),(x+w , y+h),(80,0,0),2)
##
##rect = cv2.minAreaRect(cnt2)
##box = cv2.boxPoints(rect)
##box = np.intp(box)#This line converts the floating-point coordinates of the corner points to integers using the np.int0 function
##im = cv2.drawContours(img_copy,[box],0,(80,0,0),2)

#cv2.imshow('RECT',img_copy)

###################### Minimum Enclosing Circle ################
##(x,y),radius = cv2.minEnclosingCircle(cnt2)
##
##center = (int(x),int(y))
##radius = int(radius)
##img_copy = cv2.circle(img_copy,center,radius,(80,0,0),2)
##
##cv2.imshow('circle',img_copy)

######################## ELLIPSE ###############################

##ellipse = cv2.fitEllipse(cnt2)
##img_copy = cv2.ellipse(img_copy,ellipse,(80,0,0),2)
##
##cv2.imshow('ELLIPSE',img_copy)

########################  LINE  #################################

rows,cols = img_copy.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt2, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img_copy = cv2.line(img_copy,(cols-1,righty),(0,lefty),(80,0,0),2)

cv2.imshow('LINE',img_copy)
