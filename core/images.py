import cv2
import matplotlib.pyplot as plt

image_path = '../assets/road.jpg'

# Read image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Create a Window
cv2.namedWindow('Window 1', cv2.WINDOW_NORMAL)

# Display image
cv2.imshow('Window 1', image)

# Wait for key press
# WARNING: Don't manually close, or it will still wait for a key press :)
k = cv2.waitKey(0) & 0xFF

# Check if pressed key is 's'
if k == ord('s'):
    # Write image to disk
    cv2.imwrite('tmp.jpg', image)

# Close all windows created by opencv
cv2.destroyAllWindows()

# Display using matplotlib
plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()
