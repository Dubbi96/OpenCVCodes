import numpy as np
import sys
import cv2

def func4():
    img1 = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

    img2 = img1[200:400, 200:400]
    img3 = img1[200:400, 200:400].copy()

    img2 += 200

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    func4()