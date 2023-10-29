import cv2
import numpy as np

img = np.zeros((300, 600, 3), np.uint8)
img[50:250, 100:500] = 255

g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thr, b_img = cv2.threshold(g_img, 40, 255, cv2.THRESH_BINARY)

cv2.imshow('binary', b_img)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(b_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(contours)
cv2.drawContours(img, contours, -1, (255, 0, 0), 2)

cv2.imshow('res', img)

cv2.waitKey(0)
cv2.destroyAllWindows()