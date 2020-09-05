import cv2 as cv
import numpy as np

'''
def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #cv.imshow('binary', binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
    binary = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow('open_demo',binary)
'''

def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    #cv.imshow('binary', binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
    binary = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow('open_demo',binary)


src = cv.imread('D:/data/ellipses.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
close_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()