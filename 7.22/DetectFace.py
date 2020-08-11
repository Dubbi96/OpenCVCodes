import sys
import cv2
import numpy as np

def detect_face():
    src=  cv2.imread('7.22/ResData/kids.png')

    if src is None:
        print('Img load failed!')
        return

    classifier = cv2.CascadeClassifier('7.22/ResData/haarcascade_frontalface_default.xml')

    if classifier.empty():
        print('XML load failed!')
        return

    faces = classifier.detectMultiScale(src)

    for (x, y, w, h) in faces:
        cv2.rectangle(src, (x, y), (x+w, y+h), (255, 0, 255), 2)

    cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_face()