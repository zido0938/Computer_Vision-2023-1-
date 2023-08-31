import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

cv.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
cv.rectangle(img, (200, 150), (300, 360), (0, 255, 0), 3)
cv.circle(img, (450, 50), 50, (255, 0, 0), -1)
cv.ellipse(img, (400, 250), (100, 50), 0, 0, 180, 255, -1)

cv.putText(img, 'HY23992', (10, 500), cv.FONT_HERSHEY_SIMPLEX,
           2, (255, 255, 255), 2)

cv.imshow('Drawing Features', img)

cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)
