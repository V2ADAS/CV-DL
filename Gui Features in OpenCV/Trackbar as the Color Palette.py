"""
Goal
• Learn to bind trackbar to OpenCV windows
• You will learn these functions : cv2.getTrackbarPos(), cv2.createTrackbar() etc.
"""
import cv2 as cv
import numpy as np

# Global variables
drawing = False
mode = True  # Drawing mode: True for drawing rectangles, False for drawing circles
ix, iy = -1, -1
brush_color = (0, 0, 255)  # Default color: red
brush_radius = 5  # Default brush radius

def nothing(x):
    pass

# Mouse callback function
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode, img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), brush_color, -1)
            else:
                cv.circle(img, (x, y), brush_radius, brush_color, -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), brush_color, -1)
        else:
            cv.circle(img, (x, y), brush_radius, brush_color, -1)

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('Paint Application')

# create trackbars for color change
cv.createTrackbar('R','Paint Application',brush_color[2],255,nothing)
cv.createTrackbar('G','Paint Application',brush_color[1],255,nothing)
cv.createTrackbar('B','Paint Application',brush_color[0],255,nothing)

# Create a trackbar for brush radius
cv.createTrackbar('Radius', 'Paint Application', brush_radius, 20, nothing)

# Create switch for choosing drawing mode
switch = 'Rect/Circle: 0-Rect, 1-Circle'
cv.createTrackbar(switch, 'Paint Application', mode, 1, nothing)

# Mouse callback
cv.setMouseCallback('Paint Application', draw)

while(1):
    cv.imshow('Paint Application',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get current positions of trackbars
    brush_color = (cv.getTrackbarPos('B', 'Paint Application'),
                   cv.getTrackbarPos('G', 'Paint Application'),
                   cv.getTrackbarPos('R', 'Paint Application'))
    brush_radius = cv.getTrackbarPos('Radius', 'Paint Application')
    mode = cv.getTrackbarPos(switch, 'Paint Application')
    
cv.destroyAllWindows()