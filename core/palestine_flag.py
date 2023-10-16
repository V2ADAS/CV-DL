import numpy as np
import cv2

# Create a gray image
img_width = 1240
img_height = 720
img = np.zeros((img_height, img_width, 3), np.uint8) + 128

width = 600
height = 300
x_start = int((img_width - width) / 2)
x_finish = x_start + width

y_start = 150
y_finish = y_start + height

# Black Box 
img = cv2.rectangle(img, (x_start, y_start), (x_finish, int(y_start + height / 3)), (0, 0, 0), -1)
# White Box
img = cv2.rectangle(img, (x_start, int(y_start + height / 3)), (x_finish, int(y_start + 2*height / 3)), (255, 255, 255), -1)
# Green Box
img = cv2.rectangle(img, (x_start, int(y_start + 2*height / 3)), (x_finish, int(y_start + 3*height / 3)), (0, 180, 0), -1)

# Red Triangle
pts = np.array([
        [x_start, y_start], [int(x_start + width / 3), int(y_start + height / 2)], [x_start, y_finish]
    ], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.fillPoly(img, [pts], (0, 0, 210))

img = cv2.putText(img, 'Palestine <3', (x_start - 80, y_finish + 120), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)

# Show final image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()