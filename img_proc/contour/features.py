import cv2
import numpy as np

img = cv2.imread('../../assets/star.jpg')
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh_img = cv2.threshold(img_g, 200, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('thresh', thresh_img)

contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# Find Moments
M = cv2.moments(cnt)

# use moment to find centroid
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

centroid = thresh_img.copy()
cv2.circle(centroid, (cx, cy), 4, 127, -1)
cv2.imshow('Centroid', centroid)

# Find area of contour
area = cv2.contourArea(cnt)
print('Area', area)

# Find perimeter (arc length)
perimeter = cv2.arcLength(cnt, True)
print('Permiter', perimeter)

# Contour Approx
epsilon = 0.005 * perimeter
approx = cv2.approxPolyDP(cnt, epsilon, True)
approx_cnt = img.copy()
cv2.drawContours(approx_cnt, [approx], 0, (0, 255, 0), 4)
cv2.imshow(f'Approximated, epsilon={epsilon}', approx_cnt)

# Convex Hull
hull = cv2.convexHull(cnt)
hull_cnt = img.copy()
cv2.drawContours(hull_cnt, [hull], 0, (0, 255, 0), 4)
cv2.imshow('Hull', hull_cnt)

# Bounding Rect
bounds = img.copy()
x,y,w,h = cv2.boundingRect(cnt)
st_bounding = cv2.rectangle(bounds, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Bounds', st_bounding)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.intp(box)
rt_bounding = cv2.drawContours(st_bounding, [box], 0, (0, 0, 255), 2)
cv2.imshow('Bounds', rt_bounding)

# Enclosing Circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
circ = img.copy()
circ = cv2.circle(circ, center, radius, (255, 0, 255), 3)
cv2.imshow('Enclosing Circle', circ)

# Ellipse
ellipse = cv2.fitEllipse(cnt)
elps = img.copy()
elps = cv2.ellipse(elps, ellipse, (255, 255, 0), 3)
cv2.imshow('Ellipse', elps)

# Fit Line
rows, cols = thresh_img.shape[:2]
vx, vy, x, y = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
left_y = int(((-x*vy/vx) + y)[0])
righy_y = int((((cols-x)*vy/vx) + y)[0])
l_img = thresh_img.copy()
l_img = cv2.line(l_img, (cols-1, righy_y), (0, left_y), (0, 127, 0), 2)
cv2.imshow('Line', l_img)

cv2.waitKey(0)
cv2.destroyAllWindows()