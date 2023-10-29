import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg',0)
#rows,cols = img.shape
#M = np.float32([[1,0,100],[0,1,50]])
#dst = cv2.warpAffine(img,M,(cols,rows))

rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/4,rows/2),30,1)

#the last parameter It determines the size of the output image relative to the original image
#/2 to get the center of rotation
dst = cv2.warpAffine(img,M,(cols,rows))

img = cv2.imread('drawing.png')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
