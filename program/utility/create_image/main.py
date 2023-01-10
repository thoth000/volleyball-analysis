import cv2
import numpy as np

width  = 1920
height = 1080

output = np.zeros((height, width, 3)) + 255

old = cv2.imread("old.png")
new = cv2.imread("new.png")

cv2.imwrite("output.png", old-new)