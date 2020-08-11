import cv2
import numpy as np
def affine_flip():
    src = cv2.imread('7.21/res/eastsea.bmp')
    if src is None:
        print('Image load failed')
        return
    cv2.imshow('src', src)

    for flip_code in [1, 0, 1]:
        dst = cv2.flip(src, flip_code)
        desc = 'flipcode: %d' %flip_code
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255, 0, 0), 1, cv2.LINE_AA)
    
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    affine_flip()
