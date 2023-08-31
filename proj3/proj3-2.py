import cv2 as cv
import numpy as np

def compute_pca_sift_descriptors(image, keypoints):  # 첫 조건대로 41x41크기로 추출하여 Sobel과 Normalization을 활용
    descriptors = []
    for keypoint in keypoints:
        # Convert the keypoint coordinates to integers
        x = int(keypoint.pt[0])
        y = int(keypoint.pt[1])

        # Extract a 41x41 window centered at the keypoint
        window = image[y-20:y+21, x-20:x+21]

        # Verify that the window has a valid size
        if window.shape[0] != 41 or window.shape[1] != 41:
            continue

        # Compute dy and dx using Sobel masks
        dy = cv.Sobel(window, cv.CV_32F, 0, 1, ksize=3)
        dx = cv.Sobel(window, cv.CV_32F, 1, 0, ksize=3)

        # Construct the 39x39x2-dimensional feature vector
        feature_vector = np.stack((dy.flatten(), dx.flatten()), axis=1)

        # Compute the norm of the feature vector
        norm = np.linalg.norm(feature_vector, axis=1)

        # Avoid division by zero
        norm[norm == 0] = 1.0

        # Normalize the gradient vectors of each pixel
        feature_vector = feature_vector / norm[:, np.newaxis]

        # Append the feature vector to the descriptors list
        descriptors.append(feature_vector.flatten())

    return np.array(descriptors)


img1 = cv.imread('box.png', cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('box_in_scene.png', cv.IMREAD_GRAYSCALE) # trainImage

# Initiate SIFT detector
sift = cv.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Compute PCA-SIFT descriptors
pca_sift_des1 = compute_pca_sift_descriptors(img1, kp1)
pca_sift_des2 = compute_pca_sift_descriptors(img2, kp2)

# BFMatcher with default params
bf = cv.BFMatcher()

# Match SIFT descriptors
matches_sift = bf.knnMatch(des1, des2, k=2)

# Get the minimum number of keypoints between the two images
min_keypoints = min(len(pca_sift_des1), len(pca_sift_des2))

# Set the desired size for the descriptors
descriptor_size = 20  # 조건대로 20차원으로 줄였는데 그래서인지 PCA-SIFT가 하나의 점으로 모이는 것을 관측할 수 있었다.

# Select a subset of keypoints to match
pca_sift_des1_subset = []
pca_sift_des2_subset = []

for i in range(min_keypoints):
    des1_size = pca_sift_des1[i].shape[0]
    des2_size = pca_sift_des2[i].shape[0]

    if des1_size > 0 and des2_size > 0:
        # Truncate or pad the descriptors to the desired size
        if des1_size < descriptor_size:
            des1 = np.pad(pca_sift_des1[i], (0, descriptor_size - des1_size), mode='constant')
        else:
            des1 = pca_sift_des1[i][:descriptor_size]

        if des2_size < descriptor_size:
            des2 = np.pad(pca_sift_des2[i], (0, descriptor_size - des2_size), mode='constant')
        else:
            des2 = pca_sift_des2[i][:descriptor_size]

        pca_sift_des1_subset.append(des1)
        pca_sift_des2_subset.append(des2)

# Check if either pca_sift_des1_subset or pca_sift_des2_subset is empty
if len(pca_sift_des1_subset) == 0 or len(pca_sift_des2_subset) == 0:
    print("One or both PCA-SIFT descriptor subsets are empty.")
    exit(1)

# Convert the descriptors to a single numpy array
pca_sift_des1_array = np.vstack(pca_sift_des1_subset)
pca_sift_des2_array = np.vstack(pca_sift_des2_subset)

# Convert the numpy arrays to cv::UMat // knnMatch를 사용할때 형식이 UMat일 필요가 있는 듯 하다.
pca_sift_des1_mat = cv.UMat(pca_sift_des1_array)
pca_sift_des2_mat = cv.UMat(pca_sift_des2_array)

# Perform k-NN matching with PCA-SIFT descriptors
matches_pca_sift = bf.knnMatch(pca_sift_des1_mat, pca_sift_des2_mat, k=2)

# Apply ratio test for SIFT descriptors // 조건대로 T=0.7
sift = []  # SIFT
for m, n in matches_sift:
    if m.distance < 0.7 * n.distance:
        sift.append([m])

# Apply ratio test for PCA-SIFT descriptors // 조건대로 T=0.7
pca_sift = []  #PCA-SIFT
for m, n in matches_pca_sift:
    if m.distance < 0.7 * n.distance:
        pca_sift.append([m])

# Draw matching results using SIFT descriptors
img3_sift = cv.drawMatchesKnn(img1, kp1, img2, kp2, sift, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.imwrite('sift.jpg', img3_sift)

# Draw matching results using PCA-SIFT descriptors
img3_pca_sift = cv.drawMatchesKnn(img1, kp1, img2, kp2, pca_sift, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.imwrite('sift-pca.jpg', img3_pca_sift)

# Find common matches between SIFT and PCA-SIFT descriptors
common_matches = []
for match_sift in sift:
    sift_query_idx = match_sift[0].queryIdx
    sift_train_idx = match_sift[0].trainIdx
    sift_keypoint = kp1[sift_query_idx]

    for match_pca_sift in pca_sift:
        pca_sift_query_idx = match_pca_sift[0].queryIdx
        pca_sift_train_idx = match_pca_sift[0].trainIdx
        pca_sift_keypoint = kp1[pca_sift_query_idx]

        if sift_keypoint.pt == pca_sift_keypoint.pt:
            common_matches.append(match_sift)

# Draw common matches
img3_common = cv.drawMatchesKnn(img1, kp1, img2, kp2, common_matches, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.imwrite('common.jpg', img3_common)

# Print statistics
print("Number of SIFT pairs:", len(sift))
print("Number of PCA-SIFT pairs:", len(pca_sift))
print("Number of common pairs between SIFT and PCA-SIFT:", len(common_matches))


# Measure execution time for SIFT matching
start_time_sift = cv.getTickCount()
bf.knnMatch(des1, des2, k=2)
end_time_sift = cv.getTickCount()
execution_time_sift = (end_time_sift - start_time_sift) / cv.getTickFrequency()
print("Execution time for SIFT matching:", execution_time_sift, "seconds")

# Measure execution time for PCA-SIFT matching
start_time_pca_sift = cv.getTickCount()
bf.knnMatch(pca_sift_des1_mat, pca_sift_des2_mat, k=2)
end_time_pca_sift = cv.getTickCount()
execution_time_pca_sift = (end_time_pca_sift - start_time_pca_sift) / cv.getTickFrequency()
print("Execution time for PCA-SIFT matching:", execution_time_pca_sift, "seconds")


