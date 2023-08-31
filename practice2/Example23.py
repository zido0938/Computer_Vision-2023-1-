import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Erica.jpg') 
img2=img[img.shape[0]//2:2*img.shape[0]//2,
                           img.shape[1]//4:3*img.shape[1]//4, :]
h=cv.calcHist([img],[2],None,[256],[0,256])  
plt.plot(h,color='r',linewidth=1)
cv.waitKey(1)