import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('width: %s, height: %s, channel: %s'%(width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 -pv
    cv.imshow('pixels_demo', image)


def creat_image():
    img = np.zeros([400, 400, 3], np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    cv.imshow('new_image', img)


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
t1 = cv.getTickCount()
creat_image()
access_pixels(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()*1000
print('time:%s ms'%(time))
cv.waitKey(0)
cv.destroyAllWindows()