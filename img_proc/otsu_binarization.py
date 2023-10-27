import cv2
import numpy as np
import matplotlib.pyplot as plt

# Generate a bimodal image
img = np.random.normal(100, 20, size=(300, 300)).round().astype(np.uint8)
img[80:220, 80:220] += 50

# Global Thresholding
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu's Thresholding
ret2, thresh2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Otsu's Thresholding after guassian filter
blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, thresh3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

images = [
    img, 0, thresh1,
    img, 0, thresh2,
    blur, 0, thresh3,
]

titles = [
    'Orig Noise', 'Hist', 'Global Thresh',
    'Orig Noise', 'Hist', 'Otsu Thresh',
    'Orig Filtered', 'Hist', 'Otsu Thresh Filter',
]

for i in range(3):
    plt.subplot(3, 3, i*3 + 1)
    plt.imshow(images[i*3], 'gray')
    plt.xticks([]); plt.yticks([])
    plt.subplot(3, 3, i*3 + 2)
    plt.hist(images[i*3].ravel(), 256)
    plt.subplot(3, 3, i*3 + 3)
    plt.imshow(images[i*3 + 2], 'gray')
    plt.xticks([]); plt.yticks([])

plt.show()