import cv2 as cv

img = cv.imread('stddev30.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print('File not found')
    
gImg1 = cv.GaussianBlur(img, (5,5), 0.0)
gImg2 = cv.GaussianBlur(img, (9,9), 0.0)
gImg3 = cv.GaussianBlur(img, (15,15), 0.0)
gImg4 = cv.GaussianBlur(img, (27,27), 0.0)
    
titles = ['original', 'GaussianBlur5', 'GaussianBlur9',
          'GaussianBlur15', 'GaussianBlur27']
images = [img, gImg1, gImg2, gImg3, gImg4]    
    
for i in range(5):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)