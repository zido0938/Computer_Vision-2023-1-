import cv2 as cv
import numpy as np

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print('File not found')
    
# add noise to img
img32 = np.float32(img)    
noise = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)

cv.randn(noise, 0, 5)    
noiseimg = np.uint8(np.clip(cv.add(img32, noise), 0, 255))

# apply gaussian filter 
gImg = cv.GaussianBlur(noiseimg, (5,5), 0.0)

# apply bilateral filter
bImg = cv.bilateralFilter(noiseimg, -1, 10, 5)
   
titles = ['original', 'noise', 'GaussianBlur',
          'BilateralFilter']
images = [img, noiseimg, gImg, bImg]    
    
for i in range(4):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)