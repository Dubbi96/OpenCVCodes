import numpy as np
import cv2
import sys


def blurring_mean():
    src = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return
    
    cv2.imshow('src', src)

    for ksize in (3, 5, 7):
        dst = cv2.blur(src, (ksize, ksize))

        desc = "Mean: %dx%d" % (ksize, ksize)
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    blurring_mean()