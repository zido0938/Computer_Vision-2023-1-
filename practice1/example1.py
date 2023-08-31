import cv2 as cv
import sys

img = cv.imread('Erica.jpg')

if img is None:
    sys.exit('No file found')

cv.imshow('HY23992', img)

cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)