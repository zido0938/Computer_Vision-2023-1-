import cv2 as cv

img = cv.imread('Erica.jpg')

if img is None:
    print('No file found')
    
BrushSize=5
LColor,RColor=(255,0,0),(0,0,255)

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),BrushSize,LColor,-1)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),BrushSize,RColor,-1)
    elif event==cv.EVENT_MOUSEMOVE:
        if flags==cv.EVENT_FLAG_LBUTTON:
            cv.circle(img,(x,y),BrushSize,LColor,-1)
        elif flags==cv.EVENT_FLAG_RBUTTON:
            cv.circle(img,(x,y),BrushSize,RColor,-1)
    cv.imshow('Painting', img)
    
cv.namedWindow('Painting')
cv.imshow('Painting', img)
cv.setMouseCallback('Painting', painting)

while(True):
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()
cv.waitKey(1)
