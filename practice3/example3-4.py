import cv2 as cv
import numpy as np

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("file not found")

bImg = cv.blur(img, (5,5))    

sumimg = cv.integral(img)
bImg2 = np.zeros((img.shape[0], img.shape[1]))

# write filtering with a 5x5 using sumimg

titles = ['Original Image','Blurred', 'With IntegralImg']
images = [img, bImg, bImg2]

for i in range(3):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)