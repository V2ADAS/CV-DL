import cv2
import numpy as np

def otsu_threshold_optimized(image):
    # Calculate the histogram directly using NumPy
    hist = np.histogram(image.ravel(), bins=256, range=(0, 256))[0]

    # Calculate the cumulative distribution function (CDF)
    cdf = hist.cumsum()

    # Total number of pixels in the image
    total_pixels = image.size

    # Calculate the cumulative sum of pixel values
    cdf_sum = np.arange(256) * hist

    # Find the optimal threshold
    max_variance = 0
    threshold = 0

    for t in range(256):
        if cdf[t] == 0 or cdf[t] == total_pixels:
            continue

        w0 = cdf[t] / total_pixels
        w1 = 1 - w0

        mean0 = cdf_sum[t] / cdf[t]
        mean1 = (cdf_sum[255] - cdf_sum[t]) / (total_pixels - cdf[t])

        variance = w0 * w1 * (mean0 - mean1) ** 2

        if variance > max_variance:
            max_variance = variance
            threshold = t

    return threshold

# Load the image
img = cv2.imread('noisy2.png', 0)

# Apply the optimized Otsu's threshold
otsu_threshold = otsu_threshold_optimized(img)

# Apply thresholding
ret, otsu = cv2.threshold(img, otsu_threshold, 255, cv2.THRESH_BINARY)

print("Optimized Otsu's Threshold:", otsu_threshold)

# Display the result
cv2.imshow('Original Image', img)
cv2.imshow("Otsu's Binarization", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()