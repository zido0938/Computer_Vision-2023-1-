import cv2 as cv
import numpy as np

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)

if img is None:
    print("File not found")

bImg1 = cv.blur(img, (5, 5))

suming = cv.integral(img)

bImg2 = np.zeros((img.shape[0], img.shape[1]))

# write filtering with a 5x5 using suming
for i in range(2, img.shape[0]-2):
    for j in range(2, img.shape[1]-2):
        # integral
        box_sum = (suming[i+2, j+2] - suming[i+2, j-3] - suming[i-3, j+2] + suming[i-3, j-3])
        bImg2[i, j] = box_sum / 25

bImg2 = cv.convertScaleAbs(bImg2)

titles = ['Original Image', 'Blurred (using blur function)', 'Blurred (using integral image)']
images = [img, bImg1, bImg2]

for i in range(3):
    cv.imshow(titles[i], images[i])

cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)
