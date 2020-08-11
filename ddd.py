import cv2
import numpy as np

def ddd():
    src = cv2.imread('/home/ubuntu/Desktop/screenshot.png')

    for i in range(1,100):
        cv2.imshow('frame %d' %(i), src)

    while True:
        if cv2.waitKey() == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ddd()