import cv2
import numpy as np
import sys
import random

img = cv2.imread('7.22/res/circuit.bmp', cv2.IMREAD_COLOR)
temp1 = cv2.imread('7.22/res/crystal.bmp', cv2.IMREAD_COLOR)
if img is None or temp1 is None:
    print('Img load failed!')
    sys.exit()


img = img + (50, 50, 50)
noise = np.zeros(img.shape, np.int32)
cv2.randn(noise, 0, 10)

img = cv2.add(img, noise, dtype = cv2.CV_8UC3)
res = cv2.matchTemplate(img, temp1, cv2.TM_CCOEFF_NORMED)
res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
_, maxv, _, maxloc = cv2.minMaxLoc(res)

print('maxv:', maxv)
(th, tw) = temp1.shape[:2]
cv2.rectangle(img, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

cv2.imshow('temp1', temp1)
cv2.imshow('res_norm', res_norm)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()