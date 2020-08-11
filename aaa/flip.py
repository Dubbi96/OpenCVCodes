import cv2
import numpy as np
def affine_flip():
    src = cv2.imread('aaa/21_25_180deg.png')
    if src is None:
        print('Image load failed')
        return
    cv2.imshow('src', src)

    for flip_code in [1, 0, 1]:
        dst = cv2.flip(src, flip_code)
    
    cv2.imshow('dst', dst)
    cv2.imwrite('fliped_21_25.png', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    affine_flip()
