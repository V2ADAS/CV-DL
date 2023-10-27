import cv2
import numpy as np

img = cv2.imread('../assets/road.jpg', 0)
cv2.imshow('orig', img)

kernel = np.ones((5, 5), np.uint8)

# Erode(Blacken/make zero) pixels where kernel has any zero
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('eroded', erosion)

# Opposite of erosion, dilate (Whiten/make one) pixels where kernel has any one
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('dilated', dilation)
cv2.waitKey(0)

# erode then dilate, remove surrounding noise points
openning = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('open', openning)

# dilate then erode, fill noise holes in object
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('close', closing)
cv2.waitKey(0)

# diff between dilation and erosion (mostly edge)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', gradient)

# diff between openning and original
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('top hat', top_hat)

# diff between closing and original
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('black hat', black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
ellip_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
