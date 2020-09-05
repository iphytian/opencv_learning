import cv2 as cv
import numpy as np


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print('threshold value:%s'%ret)
    cv.imshow('binary image',binary)
    coutours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(coutours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w,h)/max(w,h)
        print('rectangle rate:%s'%rate)
        mm = cv.moments(contour)
        type(mm)
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst,(np.int(cx), np.int(cy)), 3, (0,255,255), -1)
        cv.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)
        print('counter area %s'%area)
        approCurve = cv.approxPolyDP(contour, 4, True)
        if approCurve.shape[0] > 6:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
        if approCurve.shape[0] == 4:
            cv.drawContours(dst, countours, i, (0, 0, 255), 2)
    cv.imshow('meature-contours',dst)


src = cv.imread('D:/opencv-4.4.0/opencv-4.4.0/samples/data/pic5.png')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
measure_object(src)
cv.waitKey(0)
cv.destroyAllWindows()