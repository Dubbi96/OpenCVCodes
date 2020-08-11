import numpy as np
import cv2
import sys

def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize -1
    if bsize < 3:
          bsize = 3
    
    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_OTSU, bsize, 5) #cv2.THRESH_BINARY --> cv2.THRESH_OTSU 사용 가능

    cv2.imshow('dst', dst)

src = cv2.imread('7.21/res/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv2.setTrackbarPos('Block Size', 'dst', 11)
cv2.waitKey()
cv2.destroyAllWindows()
