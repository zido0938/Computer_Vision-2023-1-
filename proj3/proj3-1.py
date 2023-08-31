import cv2 as cv
import numpy as np

def kmeans_segmentation(image, k):   # kmeans_segmentation 구현
    
    pixels = image.reshape((-1, 3)).astype(np.float32)

    # Perform K-means clustering
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv.kmeans(pixels, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    # Convert centers to uint8 and reshape labels
    centers = np.uint8(centers)
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)

    return segmented_image


image = cv.imread('home.jpg')

# Perform segmentation with different values of k
k_values = [2, 4, 6, 8]
segmented_images = []
for k in k_values:
    segmented_image = kmeans_segmentation(image, k)
    segmented_images.append(segmented_image)


stacked_image = np.vstack([np.hstack(segmented_images[:2]), np.hstack(segmented_images[2:])])


cv.imshow('Segmentation Result', stacked_image)
cv.imwrite('kmeans.jpg', stacked_image)
cv.waitKey(0)
cv.destroyAllWindows()
