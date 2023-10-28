import cv2
import numpy as np

img = cv2.imread('../assets/sudoku.jpg', 0)
cv2.imshow('original', img)
cv2.namedWindow('playground')

cv2.createTrackbar('thresh1', 'playground', 0, 255, lambda x: ...)
cv2.createTrackbar('thresh2', 'playground', 0, 255, lambda x: ...)
cv2.createTrackbar('L2', 'playground', 0, 1, lambda x: ...)

while (1):
    edges = cv2.Canny(
        img,
        cv2.getTrackbarPos('thresh1', 'playground'),
        cv2.getTrackbarPos('thresh2', 'playground'),
        L2gradient=cv2.getTrackbarPos('L2', 'playground') == 1
    )
    cv2.imshow('playground', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        break
cv2.destroyAllWindows()