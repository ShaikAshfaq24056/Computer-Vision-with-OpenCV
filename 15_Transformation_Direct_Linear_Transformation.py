#Perform transformation using Direct Linear Transformation.

import cv2
import numpy as np
img1 = cv2.imread("C:/Users/ashfa/Downloads/IMG_20230825_111703.jpg")
img2 = cv2.imread("C:/Users/ashfa/Downloads/IMG_20230825_111703.jpg")
pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]])
H, _ = cv2.findHomography(pts1, pts2)
dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
img = cv2.resize(img1,(600,600))
img3 = cv2.resize(img2,(600,600))
img4 = cv2.resize(dst,(600,600))
cv2.imshow('img1', img)
cv2.imshow('img2', img3)
cv2.imshow('dst', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
