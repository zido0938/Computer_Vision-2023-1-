import cv2 as cv
import numpy as np

img = cv.imread('foldingScreen.jpg')

# 이미지를 반으로 줄임
img = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# 검은 배경 이미지 생성
bg = np.zeros((img.shape[0]*2, img.shape[1]*2, 3), dtype=np.uint8)

# 이미지를 중앙에 위치시킴
x_offset = int((bg.shape[1] - img.shape[1])/2)
y_offset = int((bg.shape[0] - img.shape[0])/2)
bg[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img

# Perspective 변환 적용
rows, cols, ch = bg.shape
pts1s = [np.float32([[200,100],[250,100],[200,300],[250,300]]),
         np.float32([[250,100],[300,100],[250,300],[300,300]]),
         np.float32([[300,100],[350,100],[300,300],[350,300]]),
         np.float32([[350,100],[400,100],[350,300],[400,300]]),
         np.float32([[400,100],[450,100],[400,300],[450,300]]),
         np.float32([[450,100],[500,100],[450,300],[500,300]]),
         np.float32([[500,100],[550,100],[500,300],[550,300]]),
         np.float32([[550,100],[600,100],[550,300],[600,300]])]

pts2s = [np.float32([[200,100],[250,75],[200,300],[250,325]]),
         np.float32([[250,75],[300,100],[250,325],[300,300]]),
         np.float32([[300,100],[350,75],[300,300],[350,325]]),
         np.float32([[350,75],[400,100],[350,325],[400,300]]),
         np.float32([[400,100],[450,75],[400,300],[450,325]]),
         np.float32([[450,75],[500,100],[450,325],[500,300]]),
         np.float32([[500,100],[550,75],[500,300],[550,325]]),
         np.float32([[550,75],[600,100],[550,325],[600,300]])]

dsts = []
for i in range(8):
    M = cv.getPerspectiveTransform(pts1s[i], pts2s[i])
    dst = cv.warpPerspective(bg, M, (cols, rows))
    dsts.append(dst[:,(i*50+200):(i*50+251),:])

result = np.hstack(dsts)

cv.imshow('folding2', result)
cv.waitKey()
cv.destroyAllWindows()
cv.waitKey(1)
