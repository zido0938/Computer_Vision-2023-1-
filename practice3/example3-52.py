import cv2 as cv

img = cv.imread('sudoku.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print("file not found")
    
ret,thresh1 = cv.threshold(img,100,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,50,255,cv.THRESH_BINARY)

thresh3 = cv.adaptiveThreshold(img, 255, 
                               cv.ADAPTIVE_THRESH_MEAN_C,
                               cv.THRESH_BINARY, 11, 2)
thresh4 = cv.adaptiveThreshold(img, 255, 
                               cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv.THRESH_BINARY, 11, 2)

titles = ['Original Image','Binary100','Binary50',
          'Adaptive mean','Adaptive Gaussian']
images = [img, thresh1, thresh2, thresh3, thresh4]

for i in range(5):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)
