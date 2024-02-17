import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('opencv_logo.png')


noise = np.random.normal(0, 1, img.shape).astype(np.uint8)

# Add the noise to the image
noisy_img = cv2.addWeighted(img, 0.5, noise, 0.5, 0)

# Display the noisy image
##cv2.imshow('Noisy Image', noisy_img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

median = cv2.medianBlur(noisy_img,5)

blur = cv2.blur(noisy_img,(5,5))
blur = cv2.GaussianBlur(noisy_img,(5,5),0)

blur1 = cv2.bilateralFilter(noisy_img,9,75,75)

plt.subplot(221),plt.imshow(noisy_img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(median),plt.title('median')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur),plt.title('blur')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur1),plt.title(' bilateral')
plt.xticks([]), plt.yticks([])

plt.show()

