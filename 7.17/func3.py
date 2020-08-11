import numpy as np
import sys
import cv2

def func3():
    img1 = cv2.imread('7.17/cat.jpg', -1)

    if img1 is None:
        print('Image load failed!')
        return

    img2 = img1
    img3 = img2.copy()

    img1[:, :] = (0, 255, 255) # Yellow

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__' :
    func3()
