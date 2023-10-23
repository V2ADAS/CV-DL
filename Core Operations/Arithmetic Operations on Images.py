"""
Goal
• Learn several arithmetic operations on images like addition, subtraction, bitwise operations etc.
• You will learn these functions : cv2.add(), cv2.addWeighted() etc.
"""
import cv2
import numpy as np
import os
import glob
import time

img1 = cv2.imread('elzaeem.jpg')
img2 = cv2.imread('palestine_flag.jpeg')
# there was an error adding them coz of different size so the solution is to resize one of them
if img1.shape != img2.shape:
    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
# Addition of two images
dst = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow("Addition", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

### Exercise ###
"""
Create a slide show of images in a folder with smooth transition between images using cv2.addWeighted function
"""
image_folder = 'C:\\Users\\engmo\\OneDrive\\Pictures\\Camera Roll'
images = sorted(glob.glob(os.path.join(image_folder, '*.JPG')))

# Ensure images are sorted in the desired order
images.sort()

transition_duration = 0.1

# Get the dimensions of the first image to use as the common size
img1 = cv2.imread(images[0])
common_size = (img1.shape[1], img1.shape[0])

# Create a loop to display the slideshow with smooth transitions
for i in range(len(images)):
    img1 = cv2.imread(images[i])
    img1 = cv2.resize(img1, common_size)  # Resize to the common size

    # If it's the last image, set img2 to the first image for a circular slideshow
    if i == len(images) - 1:
        img2 = cv2.imread(images[0])
    else:
        img2 = cv2.imread(images[i + 1])
    img2 = cv2.resize(img2, common_size)  # Resize to the common size

    # Initialize alpha for transition
    alpha = 0.0

    # Create a loop for smooth transition
    while alpha <= 1.0:
        # Perform the weighted addition with smooth transition
        blended_image = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)

        # Show the blended image
        cv2.imshow('Slideshow', blended_image)
        cv2.waitKey(1)  # Adjust delay as needed for smooth transition

        # Increase alpha for smooth transition
        alpha += 0.01
        time.sleep(transition_duration / 100.0)  # Adjust for the desired transition speed

    # Display each image for a certain duration before moving to the next one
    cv2.imshow('Slideshow', img1)
    cv2.waitKey(1000)  # Adjust the duration in milliseconds

# Close the OpenCV window after the slideshow
cv2.destroyAllWindows()