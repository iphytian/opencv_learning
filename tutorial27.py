import cv2 as cv
import numpy as np
import pytesseract as tess
from PIL import Image

def recognize_text(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(1,2))
    bin1 = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow('binary_image', open_out)

    cv.bitwise_not(open_out,open_out)
    textImage = Image.fromarray(open_out)
    text = tess.image_to_string(textImage)
    print('result:%s'%text)

src = cv.imread('D:/data/yzm1.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
recognize_text(src)
cv.waitKey(0)
cv.destroyAllWindows()