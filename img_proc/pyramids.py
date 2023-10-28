import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../assets/image.png', 0)
layer_1 = cv2.pyrDown(img)
layer_2 = cv2.pyrDown(layer_1)

cv2.imshow('Base', img)
cv2.imshow('Layer 1', layer_1)
cv2.imshow('Layer 2', layer_2)

cv2.waitKey(0)

laplacian_1 = layer_1 - cv2.pyrUp(cv2.pyrDown(layer_1))
cv2.imshow('laplacian 1', laplacian_1)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Image Blending
img1 = cv2.imread('../assets/image.png')
img2 = cv2.imread('../assets/image.png')[::-1, :, [1, 2, 0]]

mid_col = int(img1.shape[1] / 2)

direct_stitching = np.hstack([img2[:, :mid_col, :], img1[:, mid_col:, :]])

G = img1.copy()
gp1 = [G]
for i in range(5):
    G = cv2.pyrDown(G)
    gp1.append(G)
    cv2.imshow(f'Gaussian Pyramid {i}', G)

cv2.waitKey(0)
cv2.destroyAllWindows()

G = img2.copy()
gp2 = [G]
for i in range(5):
    G = cv2.pyrDown(G)
    gp2.append(G)
    cv2.imshow(f'Gaussian Pyramid {i}', G)

cv2.waitKey(0)
cv2.destroyAllWindows()

lp1 = [gp1[4]]
for i in range(4, 0, -1):
    GE = cv2.pyrUp(gp1[i])
    L = cv2.subtract(gp1[i-1], GE)
    lp1.append(L)
    cv2.imshow(f'Laplacian Pyramid {i}', L)

cv2.waitKey(0)
cv2.destroyAllWindows()

lp2 = [gp2[4]]
for i in range(4, 0, -1):
    GE = cv2.pyrUp(gp2[i])
    L = cv2.subtract(gp2[i-1], GE)
    lp2.append(L)
    cv2.imshow(f'Laplacian Pyramid {i}', L)

cv2.waitKey(0)
cv2.destroyAllWindows()

LS = []
for l1, l2 in zip(lp1, lp2):
    mid_col = int(l1.shape[1] / 2)
    ls = np.hstack([l2[:, :mid_col, :], l1[:, mid_col:, :]])
    LS.append(ls)
    cv2.imshow(f'Laplacian Stitched', ls)
    cv2.waitKey(0)

cv2.destroyAllWindows()

ls_ = LS[0]
for i in range(1, 5):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])
    cv2.imshow(f'Collecting Stitches', ls_)
    cv2.waitKey(0)

cv2.destroyAllWindows()


plt.subplot(221)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')
plt.xticks([]); plt.yticks([])

plt.subplot(222)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')
plt.xticks([]); plt.yticks([])

plt.subplot(223)
plt.imshow(cv2.cvtColor(direct_stitching, cv2.COLOR_BGR2RGB))
plt.title('Direct')
plt.xticks([]); plt.yticks([])

plt.subplot(224)
plt.imshow(cv2.cvtColor(ls_, cv2.COLOR_BGR2RGB))
plt.title('Final')
plt.xticks([]); plt.yticks([])

plt.show()