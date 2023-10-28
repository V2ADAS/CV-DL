import cv2
import numpy as np

img = cv2.imread('../assets/sudoku.jpg', 0)
edges = cv2.Canny(img, 50, 100, L2gradient=True)

cv2.imshow('Original', img)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()