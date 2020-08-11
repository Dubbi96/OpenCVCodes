import numpy as np
import sys
import cv2

def func2():
    img1 = np.empty((480, 640), np.uint8)   #graysacle
    img2 = np.zeros((480, 640, 3), np.uint8)#color
    img3 = np.ones((480, 640), np.uint8)    #1's mat
    img4 = np.full((480, 640), 0, np.float32)#Fill with 0.0
    mat1 = np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]]).astype(np.uint8)

    mat1[0,1] = 100 #element at x=1,y=0
    mat1[2,:] = 200

    print(img3)
    print(mat1)
    cv2.imshow('img1', img1)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imshow('img2', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imshow('img4', img4)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imshow('img3', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    func2()