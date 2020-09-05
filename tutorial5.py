import cv2 as cv
import numpy as np


def fill_color(image):
    copying = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copying, mask, (30,30), (0,255,255), (100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo',copying)


def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:]=255
    cv.imshow('fill_binary',image)

    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image, mask, (200,200), (0,0,255), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_binary',image)


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
#fill_color(src)
fill_binary()

'''
face = src[20:300,50:250]
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src[20:300,50:250] = backface
cv.imshow('face',src)
'''

cv.waitKey(0)
cv.destroyAllWindows()