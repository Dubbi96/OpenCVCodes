import random
import cv2
import numpy as np
import sys

def contours_basic():
    src = cv2.imread('7.22/res/contours.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Img load failed!')
        return

    contours, _ = cv2.findContours(src, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 전체 외곽선 갯수만큼 for 반복문 수행
    for i in range(len(contours)):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.drawContours(dst, contours, i, c, 2)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    contours_basic()