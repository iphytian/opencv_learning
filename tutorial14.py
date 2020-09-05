import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi - gray[row:row+ch,col:cow+col]
            ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
            gray[row:row+ch,col:cw+col] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite(‘D:/vc)


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
cv.waitKey(0)
cv.destroyAllWindows()