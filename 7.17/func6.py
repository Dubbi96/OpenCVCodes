import numpy as np
import sys
import cv2

def func6():
    mat1 = np.ones((3, 4), np.int32)
    mat2 = np.arange(12).reshape(3, 4)
    mat3 = mat1 + mat2
    mat4 = mat2 * 2

    print("mat1:", mat1, sep = '\n')
    print("mat2:", mat2, sep = '\n')
    print("mat3:", mat3, sep = '\n')
    print("mat4:", mat4, sep = '\n')

if __name__ == '__main__':
    func6()