import numpy as np
import cv2

def sobel_derivative():
    src = cv2.imread('7.21/res/lenna.bmp',cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    mx = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=np.float32)

    my = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]], dtype=np.float32)

    dx = cv2.filter2D(src, -1, mx, delta = 128)
    dy = cv2.filter2D(src, -1, my, delta = 128)

    cv2.imshow('src',src)
    cv2.imshow('dx', dx)
    cv2.imshow('dy', dy)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    sobel_derivative()