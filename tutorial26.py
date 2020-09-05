import cv2 as cv
import numpy as np


def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('D:/opencv-3.4.11/opencv-3.4.11/data/haarcascades/haarcascade_frontalface_alt_tree.xml')
    faces = face_detector.detectMultiScale(gray, 1.02, 1)
    for x,y,w,h in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow('face_detect_demo',image)


#src = cv.imread('D:/zjz.jpg')
capture = cv.VideoCapture('D:/data/vtest.avi')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
while(True):
    ret, frame = capture.read()
    frame = cv.flip(frame,1)
    face_detect_demo(frame)
    c =cv.waitKey(10)
    if c ==27:
        break


#cv.imshow('input image', src)
#face_detect_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()