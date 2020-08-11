import cv2
import numpy as np

def camera_in_video_out():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera open failed")
        return
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    delay= round(1000/fps)
    outputVideo = cv2.VideoWriter('Face.avi', fourcc, fps, (w, h))
    if not outputVideo.isOpened():
        print('File open failed!')
        return
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame
        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)
        outputVideo.write(frame)
        if cv2.waitKey(delay) == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_in_video_out()