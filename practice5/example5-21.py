#canny edge detection
import cv2 as cv
import numpy as np
img=cv.imread('apples.jpg')	

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny1=cv.Canny(gray,50,500)
canny2=cv.Canny(gray,100,200)
grad_x=cv.Sobel(gray,cv.CV_32F,1,0,ksize=3)	
grad_y=cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

fmag=cv.magnitude(grad_x,grad_y)
mag=np.uint8(fmag)

gradDir=cv.phase(grad_x,grad_y,True)

cv.imshow('mag',mag)
cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('Canny2',canny2)

cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)