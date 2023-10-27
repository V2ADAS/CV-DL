import cv2
import numpy as np

img1 = cv2.imread('../assets/road.jpg')
img2 = cv2.imread('../assets/image.png')

# Blend Two images
comb = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('blend', comb)
cv2.waitKey(0)

# Prepare logo image
img2 = cv2.resize(img2, (384, 384))

# Get ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
cv2.imshow('logo', img2)
cv2.waitKey(0)

# Create a maks for the logo
img2g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('logo', img2g)
ret, mask = cv2.threshold(img2g, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('inverted mask', mask_inv)

img1_mask_cut = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('mask cut', img1_mask_cut)

img2_mask_keep = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('mask keep', img2_mask_keep)
cv2.waitKey(0)

dst = cv2.add(img1_mask_cut, img2_mask_keep)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()