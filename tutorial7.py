import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow('noise image', image)


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
t1 = cv.getTickCount()
cv.imshow('input image', src)
#gaussian_noise(src)
dst = cv.GaussianBlur(src,(0,0),15)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print('time need: %s'%(time*1000))

cv.imshow('Guassian blur',dst)
cv.waitKey(0)
cv.destroyAllWindows()