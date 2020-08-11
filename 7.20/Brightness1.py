import numpy as np
import cv2

def brightness1():
    src = cv2.imread('Lenna.png',cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dst = cv2.add(src, 100)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    brightness1()