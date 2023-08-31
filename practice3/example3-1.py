import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print('File not found')
    
img32 = np.float32(img)
noise = np.zeros((img.shape[0], img.shape[1]), np.float32)

cv.randn(noise, 100, 50)
noiseimg1 = np.uint8(np.clip(cv.add(img32, noise), 0, 255))

cv.randn(noise, 0, 20)
noiseimg2 = np.uint8(np.clip(cv.add(img32, noise), 0, 255))

cv.randn(noise, 0, 30)
noiseimg3 = np.uint8(np.clip(cv.add(img32, noise), 0, 255))

titles = ['original', 'stddev50', 'stddev20', 'stddev30']
images = [img, noiseimg1, noiseimg2, noiseimg3]

# Drawing images with matplotlib
#for i in range(4):
#    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
#    plt.title(titles[i])
    #plt.xticks([]),plt.yticks([])        
#plt.show()

for i in range(4):
    cv.imshow(titles[i], images[i])
    cv.imwrite(titles[i] +'.jpg', images[i])
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)