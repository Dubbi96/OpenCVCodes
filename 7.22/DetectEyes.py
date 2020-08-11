import sys
import cv2
import numpy as np

def detect_eyes():
    src=  cv2.imread('7.22/ResData/kids.png')

    if src is None:
        print('Img load failed!')
        return

    face_classifier = cv2.CascadeClassifier('7.22/ResData/haarcascade_frontalface_default.xml')
    eye_classifier = cv2.CascadeClassifier('7.22/ResData/haarcascade_eye.xml')
    
    if face_classifier.empty() or eye_classifier.empty():
        print('XML load failed!')
        return

    faces = face_classifier.detectMultiScale(src)

    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(src, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 255), 2)

        faceROI = src[y1:y1 + h1, x1:x1 + w1]
    
        eyes = eye_classifier.detectMultiScale(faceROI)

        for (x2, y2, w2, h2) in eyes:
            center = (int(x2 + w2/2), int(y2 + h2/2))
            cv2.circle(faceROI, center, int(w2/2), (255, 0, 0), 2, cv2.LINE_AA)
        
    cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_eyes()