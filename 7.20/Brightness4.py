import numpy as np
import cv2

def brightness4():
    src = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed')
        return

    def update(pos):
        dst = cv2.add(src, pos)
        cv2.imshow('dst', dst)

    cv2.namedWindow('dst')
    cv2.createTrackbar('Brightenss', 'dst', 0, 100, update)
    update(0)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    brightness4()