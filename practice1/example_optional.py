import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
if not cap.isOpened():
    sys.exit('Cannot open camera')
    
while True:
    # Capture frame-by-frame
    ret,frame = cap.read()
    
    if not ret:
        print('Cannot receive frame')
        break
    cv.imshow('Video Display', frame)
    
    key=cv.waitKey(1)
    if key==ord('q'):
        break
    
# release the capture
cap.release()
cv.destroyAllWindows()
    