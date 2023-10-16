import cv2

img = cv2.imread('../assets/road.jpg')

# Access pixel value
print('pixel 100, 100: ', img[100, 100])

# Access single channel value
print('pixel 100, 100, red: ', img.item(100, 100, 2))

# Set channel value
img.itemset((100, 100, 2), 100)
print('Modified pixel 100, 100, red: ', img.item(100, 100, 2))

# Shape/Dimensions
print('Shape: ', img.shape)
print('No. of Elements: ', img.size)
print('Data Type: ', img.dtype)

# Region Of Interest
tree = img[225:600, 0:267]

x = 120
y = 40
print(tree.shape)
img[y:y+tree.shape[0], x:x+tree.shape[1]] = tree

# Remove Green Channel
img[:, :, 1] = 0

# Add Border
img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(150, 150, 0))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()