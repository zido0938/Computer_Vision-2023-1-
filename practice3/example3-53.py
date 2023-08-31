import cv2 as cv

img = cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print("file not found")
    
ret,thresh1 = cv.threshold(img,128,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,0, 255,cv.THRESH_BINARY+cv.THRESH_OTSU)

print('Otsu Threshold',ret)

titles = ['Original Image','Binary128','Otsu']
images = [img, thresh1, thresh2]

for i in range(3):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)