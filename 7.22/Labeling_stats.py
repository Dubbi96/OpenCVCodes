import numpy as np
import cv2

def labeling_stats():
    src = cv2.imread('7.22/res/keyboard.bmp', cv2.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed')
        return
    _, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]

        if area < 20:
            continue

        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(dst, pt1, pt2, (0, 255, 255))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    labeling_stats()