import cv2
import numpy as np

def camera_in():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera open failed")
        return
    print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame
        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)
        if cv2.waitKey(10) == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_in()