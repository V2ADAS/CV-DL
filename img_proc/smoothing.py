import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../assets/image.png')

# Manual Way
kernel = np.ones((5, 5), np.float32) / 25
img_avgd = cv2.filter2D(img, -1, kernel)

cv2.imshow('Orig', img)
cv2.imshow('Averaged', img_avgd)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Same as Normalized Average Filter Above
blur = cv2.blur(img, (5, 5))
cv2.imshow('Orig', img)
cv2.imshow('Blur', blur)
cv2.waitKey(0)

gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('Gaussian', gaussian_blur)
cv2.waitKey(0)

median_blur = cv2.medianBlur(img, 5)
cv2.imshow('Median', median_blur)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Bilateral', bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()