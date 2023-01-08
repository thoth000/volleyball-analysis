import numpy as np

# keypointsから腰座標
def getHipCoord(array):
  left  = np.array(array[11*3: 11*3+2])
  right = np.array(array[12*3: 12*3+2])
  
  ret = (left+right)/2
  return ret

# 直線上の最近点を求める
def computeClosestPoint(t1, v1, t2, v2):
  # 分子
  v1 = v1 / np.linalg.norm(v1)
  v2 = v2 / np.linalg.norm(v2)
  
  part0 = v1 - (np.dot(v2, v1) * v2)
  part1 = t2 - t1
  numerator = np.dot(part0, part1)
  
  # 分母
  denominator = 1 - (np.dot(v2, v1))**2
  
  point = t1 + (numerator/denominator) * v1
  return point

# 2直線の中点と最近点同士の誤差を返す
def getClosestPoint(t1, v1, t2, v2):
  # 最近点
  p1 = computeClosestPoint(t1, v1, t2, v2)
  p2 = computeClosestPoint(t2, v2, t1, v1)
  
  p = (p1+p2)/2
  error = np.linalg.norm(p1-p2)**2
  
  return p, error