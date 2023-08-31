import cv2 as cv
import numpy as np

img=cv.imread('apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

grad_x=cv.Sobel(gray,cv.CV_32F,1,0,ksize=3)	
grad_y=cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

fmag=cv.magnitude(grad_x,grad_y)
mag=np.uint8(fmag)

gradDir=cv.phase(grad_x,grad_y,True)

cv.imshow('Original',gray)
cv.imshow('mag',mag)

cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)