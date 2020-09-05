import cv2 as cv


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


def video_demo():
    capture = cv.VideoCapture('D:/gone.AVI')
    while(True):
        ret, frame = capture.read()
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            break


src = cv.imread('D:/zjz.jpg')
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
get_image_info(src)
video_demo()


cv.waitKey(0)
cv.destroyAllWindows()