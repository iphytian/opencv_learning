import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0,1], None, [100,256],[0,100,0,256])
    #cv.imshow('hist2d',hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title('2D hist')
    plt.show()

src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
hist2d_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()