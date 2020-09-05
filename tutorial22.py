import cv2 as cv
import numpy as np


def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.erode(binary,kernel)
    cv.imshow('erode_demo',dst)


def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.dilate(binary,kernel)
    cv.imshow('erode_demo',dst)


src = cv.imread('D:/opencv-4.4.0/opencv-4.4.0/samples/data/pic4.png')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
erode_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()