import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('sudoku.jpg')
rows,cols,ch=img.shape

pts1=np.float32([[205,210],[355,210],[200,360],[355,360]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))

upts1 = np.uint16(pts1)
for i in range(4):
    cv.circle(img,(upts1[i,0],upts1[i,1]),8,(0,255,0),-1)


plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv.waitKey(1)
