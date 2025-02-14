import numpy as np
import cv2
import sys

def on_thershold(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

filename = '7.21/res/neutrophils.png'
if len(sys.argv) > 1:
    filename = sys.argv[1]
src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Threshold', 'dst', 0, 255, on_thershold)
cv2.setTrackbarPos('Threshold', 'dst', 128)
cv2.waitKey(0)
cv2.destroyAllWindows()
