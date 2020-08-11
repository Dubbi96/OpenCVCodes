import numpy as np
import sys
import cv2

def func5():
    mat1 = np.array(np.arange(12)).reshape(3, 4)

    print('mat1:')
    print(mat1)

    h, w = mat1.shape[:2]

    mat2 = np.zeros(mat1.shape, type(mat1))

    for j in range(h):
        for i in range(w):
            mat2[j, 1] = mat1[j, i] + 10

    print('mat2:')
    print(mat2)

if __name__ == '__main__':
    func5()