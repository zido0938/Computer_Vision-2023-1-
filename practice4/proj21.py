import cv2 as cv
import numpy as np


img = cv.imread('tekapo.bmp')

# 중심점
center = (int((img.shape[1]-1)/2), int((img.shape[0]-1)/2))
#기본 중심점 그리기
cv.circle(img, center, 5, (0, 0, 255), -1)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.resizeWindow('image', 640, 320)
cv.imshow('image', img)


def make_center(event, x, y, flags, param):
    global center
    if event == cv.EVENT_LBUTTONDOWN:
        center = (x, y)
        cv.circle(img, center, 5, (0, 0, 255), -1)
        cv.imshow('image', img)


cv.setMouseCallback('image', make_center)

# geometric transformation 함수들
def translate(img, x, y):
    T = np.float32([[1, 0, x], [0, 1, y]])
    img_trans = cv.warpAffine(img, T, (img.shape[1], img.shape[0]))
    return img_trans

def rotate(img, angle):
    R = cv.getRotationMatrix2D(center, angle, 1)
    img_rot = cv.warpAffine(img, R, (img.shape[1], img.shape[0]))
    return img_rot

def scale(img, factor):
    S = np.float32([[factor, 0, 0], [0, factor, 0]])
    img_scaled = cv.warpAffine(img, S, (img.shape[1], img.shape[0]))
    return img_scaled

def shear(img, factor):
    SH = np.float32([[1, factor, 0], [0, 1, 0]])
    img_shear = cv.warpAffine(img, SH, (img.shape[1], img.shape[0]))
    return img_shear

def mirror_y(img):
    img_mirror = cv.flip(img, 1)
    return img_mirror

def mirror_x(img):
    img_mirror = cv.flip(img, 0)
    return img_mirror

def transform_x(img, factor):
    T = np.float32([[1, 0, 0], [factor, 1, 0]])
    img_trans = cv.warpAffine(img, T, (img.shape[1], img.shape[0]))
    return img_trans

def transform_y(img, factor):
    T = np.float32([[1, factor, 0], [0, 1, 0]])
    img_trans = cv.warpAffine(img, T, (img.shape[1], img.shape[0]))
    return img_trans


while True:
    key = cv.waitKey(0)
    if key == ord('q'):
        break
    elif key == ord('t'):
        img = translate(img, 5, 5)
        cv.imshow('image', img)
    elif key == ord('r'):
        img = rotate(img, 10)
        cv.imshow('image', img)
    elif key == ord('s'):
        if img.shape[1] == 640:
            img = scale(img, 0.5)
        else:
            img = scale(img, 2)
        cv.imshow('image', img)
    elif key == ord('h'):
        img = shear(img, 0.5)
        cv.imshow('image', img)
    elif key == ord('k'):
        img = mirror_y(img)
        cv.imshow('image', img)
    elif key == ord('l'):
        img = mirror_x(img)
        cv.imshow('image', img)
    elif key == ord('x'):
        img = transform_x(img, 0.1)
        cv.imshow('image', img)
    elif key == ord('y'):
        img = transform_y(img, 0.1)
        cv.imshow('image', img)
    elif key == ord('1'):
        img = translate(img, -5, -5)
        img = shear(img, -0.5)
        img = scale(img, 0.5)
        img = rotate(img, -10)
        cv.imshow('image', img)
    elif key == ord('2'):
        img = translate(img, 5, 5)
        img = shear(img, 0.5)
        img = scale(img, 2)
        img = rotate(img, 10)
        cv.imshow('image', img)
