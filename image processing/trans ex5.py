import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('edge.png')

blur = cv2.blur(img,(5,5))
blur = cv2.GaussianBlur(img,(5,5),0)

blur1 = cv2.bilateralFilter(img,9,75,75)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur1),plt.title('Blurred2')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow('img',img)
