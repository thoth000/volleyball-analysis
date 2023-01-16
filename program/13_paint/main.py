import json
import cv2
import numpy as np
from func import func

file = open("170.json")
data = json.load(file)

correspond = [
  # 首接続
  [0, 1],
  [0, 6],
  [0, 7],
  [0, 12],
  [0, 13],
  # 肩肘
  [6, 8],
  [7, 9],
  # 肘手
  [8, 10],
  [9, 11],
  # 腰腰
  [12, 13],
  # 腰膝
  [12, 14],
  [13, 15],
  # 膝足
  [14, 16],
  [15, 17]
]

img = np.array([
  [
    [255, 255, 255] for w in range(1920)
  ]
  for h in range(1080)
])

for person in data:
  black = (0, 0, 0)
  iro = np.random.rand(3)*200
  newData = func(data[person])
  for c in correspond:
    id1, id2 = c[0], c[1]
    x1 = int(newData[id1*3])
    y1 = int(newData[id1*3+1])
    
    x2 = int(newData[id2*3])
    y2 = int(newData[id2*3+1])
    
    print(x1, y1, x2, y2)
    cv2.line(img, pt1=(x1, y1), pt2=(x2, y2), color=iro, thickness=3)

  # 枠線
  x0 = int(newData[54])
  y0 = int(newData[55])
  
  w = int(newData[56])
  h = int(newData[57])
  
  cv2.line(img, pt1=(x0, y0), pt2=(x0+w, y0), color=iro, thickness=2)
  cv2.line(img, pt1=(x0+w, y0), pt2=(x0+w, y0+h), color=iro, thickness=2)
  cv2.line(img, pt1=(x0+w, y0+h), pt2=(x0, y0+h), color=iro, thickness=2)
  cv2.line(img, pt1=(x0, y0+h), pt2=(x0, y0), color=iro, thickness=2)
  
cv2.imwrite("output.png", img)
file.close()