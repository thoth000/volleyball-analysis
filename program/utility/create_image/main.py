import cv2
import numpy as np

width  = 1920
height = 1080

output = np.zeros((height, width, 3)) + 255

old = cv2.imread("old.png")
new = cv2.imread("new.png")

for i in range(height):
  print(i)
  for j in range(width):
    a = old[i][j]
    b = new[i][j]
    
    if np.linalg.norm(a-b) < 100:
      continue
    else:
      output[i][j] = b
cv2.imwrite("output.png", output)