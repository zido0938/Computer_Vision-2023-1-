import cv2 as cv
import sys
img = cv.imread('Erica.jpg')

if img is None:
    print('No file found')


# mouse callback function
def draw(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+50,y+50),(0,0,255),2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+50,y+50),(0,255,0),2)
    cv.imshow('Drawing a rectangle', img)
    
cv.namedWindow('Drawing a rectangle')
cv.imshow('Drawing a rectangle', img)
cv.setMouseCallback('Drawing a rectangle',draw)

while(True):
    if cv.waitKey(20)==ord('q'):
        break
cv.destroyAllWindows()
cv.waitKey(1)
