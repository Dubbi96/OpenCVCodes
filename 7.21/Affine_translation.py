import cv2
import numpy as np

def affine_translation():
    src = cv2.imread('7.21/res/tekapo.bmp')
    if src is None:
        print('Image load failed')
        return

    affine_mat = np.array([[1, 0, 150],
                            [0, 1, 100]]).astype(np.float32)

    dst = cv2.warpAffine(src, affine_mat, (0, 0))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    affine_translation()