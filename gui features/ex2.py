import numpy as np
import cv2

img=cv2.imread('messi5.jpg')
cv2.imshow('Image',img)

k=cv2.waitKey(0)
if k== 27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('messigray2.png',img)
    cv2.destroyAllWindows()
