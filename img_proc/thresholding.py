import cv2
import numpy as np
import matplotlib.pyplot as plt

# Generate a gradient image from black to white
img = np.tile(np.linspace(0, 255, 300, dtype=np.uint8), (300, 1))

# Apply different SIMPLE Thresholding functions
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['original', 'bin', 'bin_i', 'trunc', 'toZ', 'toZ_i']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]); plt.yticks([])

plt.show()

img = cv2.imread('../assets/sudoku.jpg', 0)
img = cv2.medianBlur(img, 5)

# Apply different ADAPTIVE Thresholding functions
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['original', 'simple', 'mean', 'gaussian']
images = [img, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]); plt.yticks([])

plt.show()