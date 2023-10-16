"""
Goals
    Here, I will learn how to read an image, how to display it and how to save it back
    You will learn these functions : cv2.imread(), cv2.imshow() , cv2.imwrite()
    I will learn how to display images with Matplotlib
"""
# Read an image

"""
Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of image should be given.
Second argument is a flag which specifies the way image should be read.
    cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
    cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load an color image in grayscale
img1 = cv.imread('elzaeem.jpg',0)

# Display an image

cv.imshow('Adel Imam',img1)
cv.waitKey(0)
"""
If i wrote cv.waitKey(1000)
it means that window will remain open for 1 second before closing automatically or i kill it before the second ends
"""
cv.destroyAllWindows()
"""
we can destry a specific window when mention its name:
    cv.destroyWindow('Adel Imam')
or we can with a specific key like escape:
    # Check the key pressed
    if key == 27:  # If the 'Esc' key (27 in ASCII) is pressed
        cv.destroyAllWindows()  # Close the window
"""
img2 = cv.imread('cat.jpg',0)
# Create a named window with cv.WINDOW_NORMAL flag (resizable)
cv.namedWindow('My Resizable Window', cv.WINDOW_NORMAL)

# Display the image in the window
cv.imshow('My Resizable Window', img2)
cv.waitKey(0)
cv.destroyAllWindows()

# Write an image
cv.imwrite("new-image.png", img2)

####  With Matplotlib
plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
"""
ooops we have a problem :
There is a slight difference in pixel ordering in OpenCV and Matplotlib.
OpenCV follows BGR order, while matplotlib likely follows RGB order.
"""
img2 = cv.imread('cat.jpg')
b,g,r = cv.split(img2)
img3 = cv.merge([r,g,b])
plt.subplot(121); plt.imshow(img2)
plt.subplot(122); plt.imshow(img3)
plt.show()
cv.imshow('bgr image',img2) # expects true color
cv.imshow('rgb image',img3) # expects distorted color
cv.waitKey(0)
cv.destroyAllWindows()

                                                # Done p.g 24 #