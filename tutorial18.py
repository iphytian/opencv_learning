import cv2 as cv
import numpy as np


def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(image,(x1,y2),(x2,y2),(0,0,255),2)
    cv.imshow('image_lines',image)


src = cv.imread('D:/opencv-4.4.0/opencv-4.4.0/samples/data/sudoku.png')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
#cv.imshow('input image', src)
line_detection(src)
cv.waitKey(0)
cv.destroyAllWindows()