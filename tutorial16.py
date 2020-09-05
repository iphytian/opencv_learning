import cv2 as cv
import numpy as np


def lapalian_demo(image):
    #dst = cv.Laplacian(image,cv.CV_32F)
    #lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lpls= cv.convertScaleAbs(dst)
    cv.imshow('lapalian',lpls)



def sobel_demo(image):
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow('grandient_x', gradx)
    cv.imshow('grandient_y', grady)
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow('gradient',gradxy)


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
#sobel_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()