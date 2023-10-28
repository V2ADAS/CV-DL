import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../assets/sudoku.jpg', 0)

laplacian = cv2.Laplacian(img, -1, ksize=5)
sobelx = cv2.Sobel(img, -1, 1, 0, ksize=5)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=5)

plt.subplot(221)
plt.imshow(img, 'gray')
plt.title('Original')
plt.xticks([]); plt.yticks([])

plt.subplot(222)
plt.imshow(laplacian, 'gray')
plt.title('Laplacian')
plt.xticks([]); plt.yticks([])

plt.subplot(223)
plt.imshow(sobelx, 'gray')
plt.title('Sobel X')
plt.xticks([]); plt.yticks([])

plt.subplot(224)
plt.imshow(sobely, 'gray')
plt.title('Sobel Y')
plt.xticks([]); plt.yticks([])

plt.show()

# Detect Missed edges because of sign and datatype conversions
box = np.zeros((300, 300), np.uint8)
box[100:200, 100:200] = 255
sobelx8u = cv2.Sobel(box, cv2.CV_8U, 1, 0, ksize=5)

sobelx64f = cv2.Sobel(box, cv2.CV_64F, 1, 0, ksize=5)
sobel_8u = np.uint8(np.absolute(sobelx64f))

plt.subplot(131)
plt.imshow(box, 'gray')
plt.title('Original')
plt.xticks([]); plt.yticks([])

plt.subplot(132)
plt.imshow(sobelx8u, 'gray')
plt.title('8U')
plt.xticks([]); plt.yticks([])

plt.subplot(133)
plt.imshow(sobel_8u, 'gray')
plt.title('64F -> 8U')
plt.xticks([]); plt.yticks([])

plt.show()