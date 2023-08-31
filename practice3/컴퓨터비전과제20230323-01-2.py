import cv2 as cv

img = cv.imread('rose.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("file not found")
img2 = cv.imread('rose.png')
if img is None:
     print("file not found")   
ret,thresh = cv.threshold(img,150, 255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img2,150, 255,cv.THRESH_BINARY)
print('Otsu Threshold',ret)

titles = ['Original Image','Otsu1(GrayScale)','Otusu2']
images = [img, thresh,thresh2]

for i in range(3):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)