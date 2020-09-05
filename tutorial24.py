import cv2 as cv
import numpy as np


def top_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    #cimage = np.array(gray.shape, np.uint8)
    cimage = 20
    cv.add(dst,cimage)
    cv.imshow('top_hat',dst)


def black_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(15,15))
    dst = cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)
    #cimage = np.array(gray.shape, np.uint8)
    cimage = 20
    cv.add(dst,cimage)
    cv.imshow('balck_hat',dst)


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
top_hat_demo(src)
black_hat_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()