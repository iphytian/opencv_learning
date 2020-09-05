import cv2 as cv
import numpy as np


def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist',dst)


def clahe_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    dst = clahe.apply(gray)
    cv.imshow('equalHist',dst)


#直方图的比较
def creat_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16,1], np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index),0] = rgbHist[np.int(index),0]+1
    return rgbHist


def hist_compare(image1, image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR)
    print('巴士距离：%s, 相关性：%s, 卡方：%s'%(match1, match2, match3))


#src = cv.imread('D:/zjz.jpg')
src = cv.imread('D:/opencv-3.3.0/samples/data/notes.png')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

image1 = cv.imread('D:/opencv-3.3.0/samples/data/lena.jpg')
image2 = cv.imread('D:/opencv-3.3.0/samples/data/lena_tmpl.jpg')
hist_compare(image1, image2)
#equalHist_demo(src)
creat_rgb_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()