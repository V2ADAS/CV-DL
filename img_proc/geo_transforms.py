import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../assets/sudoku.jpg')

# Sizing
img_resized = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resizing', img_resized)
cv2.waitKey(0)

# Translation
tx, ty = 30, 80
# transformation matrix for shifting by tx to the right, and by ty down
transformation_mat = np.float32([[1, 0, tx], [0, 1, ty]])
img_translated = cv2.warpAffine(
    img, # source image
    transformation_mat, # transformation matrix
    img.shape[1::-1], # size of the output as (width, height)
)

cv2.imshow('Translation', img_translated)
cv2.waitKey(0)

# Rotation
transformation_mat = cv2.getRotationMatrix2D(
    [i/2 for i in img.shape[1::-1]], # center of rotation (x, y)
    90, # rotation angle (counter-clockwise)
    1,
)
img_rotated = cv2.warpAffine(img, transformation_mat, img.shape[1::-1])

cv2.imshow('Rotation', img_rotated)
cv2.waitKey(0)

# Affine Transformations
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

transformation_mat = cv2.getAffineTransform(pts1, pts2)
img_transformed = cv2.warpAffine(img, transformation_mat, img.shape[1::-1])

cv2.imshow('Affine Transformation', img_transformed)
cv2.waitKey(0)

# Prespective Transformation
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

transformation_mat = cv2.getPerspectiveTransform(pts1, pts2)
img_presp = cv2.warpPerspective(img, transformation_mat, (300, 300))

cv2.imshow('Prespective Transformation', img_presp)
cv2.waitKey(0)

cv2.destroyAllWindows()