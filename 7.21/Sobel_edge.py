import numpy as np
import cv2

def sobel_edge():
    src = cv2.imread('7.21/res/lenna.bmp',cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

    fmag = cv2.magnitude(dx, dy)
    mag = np.uint8(np.clip(fmag, 0, 255))                       #편미분 값을 Grayscale image 형태로 표현
    _, edge = cv2.threshold(mag, 150, 255, cv2.THRESH_BINARY)   #mag와 같이 계산후 150이상은 흰색으로 미만은 검정으로 분류

    cv2.imshow('src', src)
    cv2.imshow('mag', mag)
    cv2.imshow('edge', edge)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    sobel_edge()