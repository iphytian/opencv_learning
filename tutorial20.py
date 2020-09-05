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
    edge_output = cv.Canny(gray, 10, 100)
    cv.imshow('canny edge',edge_output)
    return  edge_output


def contours_demo(image):
    '''
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    #cv.imshow('binary_image',binary)'''
    binary = edge_demo(image)

    contours,b= cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        print(i)
    cv.imshow('detect contours',image)


src = cv.imread('D:/opencv-4.4.0/opencv-4.4.0/samples/data/pic3.png')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()