import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3,3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # y Gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # EDGE
    #edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow('canny edge',edge_output)

    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow('color edge',dst)

src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()