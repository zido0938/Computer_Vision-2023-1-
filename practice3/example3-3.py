import cv2 as cv
import random

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print('File not found')
cv.imshow('original',img)    
# add salt and pepper noise to img
noiseNum = img.size//10

for i in range(noiseNum):
    row = random.randrange(img.shape[0])
    col = random.randrange(img.shape[1])
    img[row,col] = (i % 2) * 255    

cv.imshow('Salt and pepper noise', img)    

# Apply Gaussian Filter
gImg = cv.GaussianBlur(img, (5,5), 0.0)
# Apply Median Filter
mImg = cv.medianBlur(img, 3)
cv.imshow('Gaussian Filter ', gImg)
cv.imshow('Media Filter', mImg)

cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)