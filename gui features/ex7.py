import cv2
import numpy
import time
import timeit


# your code execution
img1 = cv2.imread('messi5.jpg')

#e1 = cv2.getTickCount()
e1=time.time()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
#e2 = cv2.getTickCount()
e2=time.time()
#time = (e2 - e1)/ cv2.getTickFrequency()
time = (e2 - e1)
print(time)
