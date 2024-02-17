import cv2
import numpy as np,sys

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')


# generate Gaussian pyramid for A

G = A.copy()
gpA = [G] 

for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)


# generate Gaussian pyramid for B

G = B.copy()
gpB = [G]

for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A

lpA = [gpA[5]]

for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    
    # Resize the image to match the size of the other image
    GE_resized = cv2.resize(GE, (gpA[i-1].shape[1], gpA[i-1].shape[0]))


    L = cv2.subtract(gpA[i-1],GE_resized)
    lpA.append(L)

# generate Laplacian Pyramid for B

lpB = [gpB[5]]

for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    # Resize the image to match the size of the other image
    GE_resized = cv2.resize(GE, (gpB[i-1].shape[1], gpB[i-1].shape[0]))
    L = cv2.subtract(gpB[i-1],GE_resized)
    lpB.append(L)
    
# Now add left and right halves of images in each level

LS = []

for la,lb in zip(lpA,lpB):
    
    rows,cols,dpt = la.shape
    # Ensure both arrays have the same shape along the 0th dimension
    min_rows = min(la.shape[0], lb.shape[0])
    la = la[:min_rows, :]
    lb = lb[:min_rows, :]
    # Concatenate the arrays horizontally
    ls = np.hstack((la[:, 0:int(cols/2)], lb[:, int(cols/2):]))
   # ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    LS.append(ls)

# now reconstruct

ls_ = LS[0]

for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    # Ensure both arrays have the same size and number of channels
    ls_ = ls_[:LS[i].shape[0], :LS[i].shape[1]]

    # Perform element-wise addition
    ls_ = cv2.add(ls_, LS[i])
    #ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half

# Ensure both arrays have the same shape along the 0th dimension
min_rows = min(A.shape[0], B.shape[0])
A = A[:min_rows, :]
B = B[:min_rows, :]

# Concatenate the arrays horizontally
real = np.hstack((A[:, :cols//2], B[:, cols//2:]))

#real = np.hstack((A[:,:cols//2],B[:,cols//2:]))
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
