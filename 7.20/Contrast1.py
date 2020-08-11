import numpy as np
import cv2

def contrast1():
    src = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
    
    if src is None:
        print('Image load failed!')
        return

    s = 2.0
    dst = cv2.multiply(src, s)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    contrast1()