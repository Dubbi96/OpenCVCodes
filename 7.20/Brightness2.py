import numpy as np
import cv2

def brightness2():
    src = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    dst = np.empty(src.shape, src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = src[y, x] + 100

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    brightness2()