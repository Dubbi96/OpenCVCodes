import numpy as np
import cv2
import sys


def blurring_gaussian():
    src = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return
    
    cv2.imshow('src', src)

    for sigma in range(1, 6):
        dst = cv2.GaussianBlur(src, (0, 0), sigma)

        desc = "Gaussian: sigma =  %d" % (sigma)
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    blurring_gaussian()