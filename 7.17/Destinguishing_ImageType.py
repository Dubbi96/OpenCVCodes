import numpy as np
import sys
import cv2

def func1():
    img1 = cv2.imread('7.17/cat.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('7.17/cat.jpg')

    if img1 is None or img2 is None:
        print('Image load failed!')
        return

    print('type(img1) : ', type(img1))
    print('img1.shape : ', img1.shape)

    print('type(img2) : ', type(img2))
    print('img2.shape : ', img2.shape)


    if len(img1.shape) == 2:
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is a truescale image')

    if len(img2.shape) == 2:
        print('img2 is a grayscale image')
    elif len(img2.shape) == 3:
        print('img2 is a truescale image')

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__' :
    func1()