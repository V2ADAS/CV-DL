import numpy
import cv2
# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)
#img2 = cv2.imread('messi5.jpg',0)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.imshow('image2',img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.namedWindow('image3', cv2.WINDOW_NORMAL)
#cv2.imshow('image3',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite('messigray.png',img)
