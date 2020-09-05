import cv2 as cv


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow('add_demo',dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow('suntract_demo',dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow('divide_demo',dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('multiply_demo',dst)


def multiply_demo(m1, m2):
    (M1, dev1) = cv.meanStdDev(m1)
    (M2, dev2) = cv.meanStdDev(m2)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)


print('------------ Hello Python -------------')
src1 = cv.imread('D:/opencv-3.3.0/samples/data/LinuxLogo.jpg')
src2 = cv.imread('D:/opencv-3.3.0/samples/data/WindowsLogo.jpg')
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow('image1', src1)
cv.imshow('image2', src2)
add_demo(src1,src2)
subtract_demo(src1,src2)
divide_demo(src1,src2)
multiply_demo(src1,src2)
cv.waitKey(0)
cv.destroyAllWindows()