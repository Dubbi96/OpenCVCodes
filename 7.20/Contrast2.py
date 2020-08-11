import numpy as np
import cv2

def contrast2():
    src = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
    
    if src is None:
        print('Image load failed!')
        return

    alpha = 100.0
    dst = np.clip(src + alpha*(src - 128.), 0, 255).astype(np.uint8)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    contrast2()