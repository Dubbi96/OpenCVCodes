import cv2
import numpy as np
import random
import sys
def coner_harris():
    src = cv2.imread('7.22/res/building.jpg', cv2.IMREAD_GRAYSCALE)
    
    if src is None:
        print('Img load failed!')
        return
    
    harris = cv2.cornerHarris(src, 3, 3, 0.04)
    harris_norm = cv2.normalize(harris, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    for y in range(harris_norm.shape[0]):
        for x in range(harris_norm.shape[1]):
            if harris_norm[y, x] > 120:
                if(harris[y, x] > harris[y-1, x] and
                    harris[y, x] > harris[y-1, x] and
                    harris[y, x] > harris[y-1, x] and
                    harris[y, x] > harris[y-1, x]):
                    cv2.circle(dst, (x, y), 5, (0, 0, 255), 2)
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.imshow('harris_norm', harris_norm)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    coner_harris()