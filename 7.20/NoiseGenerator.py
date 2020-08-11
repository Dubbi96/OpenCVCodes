import sys
import numpy as np
import cv2
import random

def noise_gaussian():
    src = cv2.imread('./7.20/Lenna.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()
    
    cv2.imshow('src', src)

    for stddev in [10, 20, 30, 50, 100]:
        noise = np.zeros(src.shape, np.int32)
        cv2.randn(noise, 0, stddev)
        print(noise)
        dst = cv2.add(src, noise, dtype = cv2.CV_8UC1)

        desc = 'stddev = %d' % stddev
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)
        cv2.imshow('dst', dst)
        cv2.waitKey()
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    noise_gaussian()