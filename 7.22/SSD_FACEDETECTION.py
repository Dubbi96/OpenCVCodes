import numpy as np
import cv2
import sys

model = '7.22/face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = '7.22/face_detector/deploy.prototxt'
# model = '7.22/face_detector/opencv_face_detector_uint8.pb'
# config = '7.22/face_detector/opencv_face_detector.pbtxt'

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

net = cv2.dnn.readNet(model, config)
if net.empty():
    print('Net open failed!')
    sys.exit()
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
outputVideo = cv2.VideoWriter('Face2.avi', fourcc, fps, (w, h))
while True:
    _, frame = cap.read()
    if frame is None:
        break
    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 177, 123))
    net.setInput(blob)
    detect = net.forward()
    (h, w) = frame.shape[:2]
    detect = detect[0, 0, :, :]
    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            break

        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * h)

        cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 0))

        label = 'Face: %4.3f' %confidence
        cv2.putText(frame, label, (x1, y1 -1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
    
    
    
    
    cv2.imshow('frame', frame)
    outputVideo.write(frame)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
