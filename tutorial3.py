import cv2 as cv
import numpy as np


def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv',yuv)


def color_object_demo():
    capture = cv.VideoCapture()
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv, lowerb=lower_hsv,upperb=upper_hsv)
        cv.imshow('vedio',frame)
        cv.imshow('mask',mask)
        c = cv.waitKey(40)
        if c == 27:
            braak


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
color_space_demo(src)

b, g, r = cv.split(src)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

cv.waitKey(0)
cv.destroyAllWindows()