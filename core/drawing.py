import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a line with two points
img = cv2.line(img, (0, 0), (511, 511), (150, 0, 150), 2)

# Draw a rectangle
img = cv2.rectangle(img, (256, 128), (384, 255), (0, 150, 0), 3)

# Draw a circle
img = cv2.circle(img, (128, 384), 181, (0, 150, 150), 3)

# Draw an ellipse
img = cv2.ellipse(img, (320, 182), (64, 128), 0, -30, 210, (200, 220, 200), -1)

# Draw a polygon
pts = np.array([
        [256, 0], [128, 511], [511, 128], [0, 128], [384, 511]
    ], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (150, 150, 150), 2)

img = cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)

# Show final image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()