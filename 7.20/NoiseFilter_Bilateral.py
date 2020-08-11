import sys
import numpy as np
import cv2
import random

def filter_bilateral():
    src = cv2.imread('./7.20/Lenna.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()
    
    cv2.imshow('src', src)

    noise = np.zeros(src.shape, np.int32)
    cv2.randn(noise, 0, 10)
    dst = cv2.add(src, noise, dtype = cv2.CV_8UC1)

    dst1 = cv2.GaussianBlur(src, (0, 0), 5)
    dst2 = cv2.bilateralFilter(dst, -1, 10, 5)

    cv2.imshow('dst', dst)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    filter_bilateral()

