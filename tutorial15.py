import cv2 as cv
import numpy as np


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_image.append(dst)
        cv.imshow('pyramid_down_'+str(i),dst)
        temp = dst.copy()
    return pyramid_image


def lapalian_demo(image):
    pyramid_image = pyramid_demo(image)
    level = len(pyramid_image)
    for i in range(level-1, -1, -1):
        if (i-1)<0:
            expand = cv.pyrUp(pyramid_image[i],dstsize=image.shape[:2])
            laps = cv.subtract(image, expand)
            cv.imshow('laps_' + str(i), laps)
        else:
            expand = cv.pyrUp(pyramid_image[i],dstsize=pyramid_image[i-1].shape[:2])
            laps = cv.subtract(pyramid_image[i-1], expand)
            cv.imshow('laps_'+str(i),laps)


src = cv.imread('D:/opencv-4.4.0/opencv-4.4.0/samples/data/lena.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
#pyramid_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()