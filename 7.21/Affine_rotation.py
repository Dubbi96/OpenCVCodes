import cv2
import numpy as np

def affine_rotation():
    src = cv2.imread('7.21/res/tekapo.bmp')
    if src is None:
        print('Image load failed')
        return
    cp = (src.shape[1] / 2, src.shape[0] / 2)
    affine_mat = cv2.getRotationMatrix2D(cp, 90, 1)
    dst = cv2.warpAffine(src, affine_mat, (0, 0))
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    affine_rotation()