import cv2
import numpy as np

def affine_transform():
    src = cv2.imread('7.21/res/tekapo.bmp')
    if src is None:
        print('Image load failed')
        return
    rows = src.shape[0]
    cols = src.shape[1]
    src_pts = np.array([[0, 0],
                        [cols - 1, 0],
                        [cols - 1, rows - 1]]).astype(np.float32)
    dst_pts = np.array([[50, 50],
                        [cols - 100, 100],
                        [cols - 50, rows - 50]]).astype(np.float32)
    
    affine_mat = cv2.getAffineTransform(src_pts, dst_pts)
    dst = cv2.warpAffine(src, affine_mat, (0, 0))
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    affine_transform()