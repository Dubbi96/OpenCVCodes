import cv2
import numpy as np
import random
cap = cv2.VideoCapture('7.22/ResData/vtest.avi')
if not cap.isOpened():
    print('Video open failed!')
    sys.exit()
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
while True:
    ret, frame = cap.read()

    if not ret:
        break

    detected, _ = hog.detectMultiScale(frame)

    for (x,y,w,h) in detected:
        c = (0, 255, 0)
        cv2.rectangle(frame, (x, y), (x + w, y + h), c, 3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()