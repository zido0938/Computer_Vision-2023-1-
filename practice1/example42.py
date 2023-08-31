import cv2 as cv
img = cv.imread('Erica.jpg')

if img is None:
    print('No file found')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imwrite('Erica.jpg', gray)
# mouse callback function
def draw(event,x,y,flags,param):
    global ix, iy;
    
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
    cv.imshow('Drawing a rectangle', img)
    
cv.namedWindow('Drawing a rectangle')
cv.imshow('Drawing a rectangle',img)
cv.setMouseCallback('Drawing a rectangle',draw)
cv.putText(img, '2021004866 JI HYEON DO', (5, 550), cv.FONT_HERSHEY_SIMPLEX,
           0.5, (0, 255, 0), 2)

while(True):
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()
cv.waitKey(1)
