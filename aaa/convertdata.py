import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import cv2
A = np.genfromtxt('aaa/1595658579.0086422.txt',dtype='str', delimiter = ' ')
B = A[:,0:2].astype(np.float64)
prv_time = time.time()
b = time.localtime()
aa = plt.scatter(B[:,0],B[:,1],s = 1)
aa = plt.axis('off')
plt.savefig('{0}_{1}.png'.format(b.tm_hour,b.tm_min))
print( time.time() - prv_time)
src = cv2.imread('{0}_{1}.png'.format(b.tm_hour,b.tm_min))
cp = (src.shape[1] / 2, src.shape[0] / 2)
affine_mat1 = cv2.getRotationMatrix2D(cp, 90, 1)
affine_mat2 = cv2.getRotationMatrix2D(cp, 180, 1)
affine_mat3 = cv2.getRotationMatrix2D(cp, 270, 1)
dst1 = cv2.warpAffine(src, affine_mat1, (0, 0))
dst2 = cv2.warpAffine(src, affine_mat2, (0, 0))
dst3 = cv2.warpAffine(src, affine_mat3, (0, 0))
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imwrite('{0}_{1}_90deg.png'.format(b.tm_hour,b.tm_min), dst1)
cv2.imwrite('{0}_{1}_180deg.png'.format(b.tm_hour,b.tm_min), dst2)
cv2.imwrite('{0}_{1}_270deg.png'.format(b.tm_hour,b.tm_min), dst3)
cv2.waitKey()
cv2.destroyAllWindows()