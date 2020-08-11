import sys
import numpy as np
import cv2
import random

def filter_median():
    src = cv2.imread('./7.20/Lenna.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()
    
    for i in range(0, int(src.size /10)):
        x = random.randint(0, src.shape[1] - 1)
        y = random.randint(0, src.shape[0] - 1)
        src[x, y] = (i % 2) * 255

    dst1 = cv2.GaussianBlur(src, (0, 0), 1)
    dst2 = cv2.medianBlur(src, 3)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    filter_median()

