import numpy as np

# https://risalc.info/src/distance-between-two-lines.html
# 最近点2点とその距離、推定位置を求める

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

def newCompute3dCoord(t1, v1, t2, v2):
  # 最近点
  p1 = computeClosestPoint(t1, v1, t2, v2)
  p2 = computeClosestPoint(t2, v2, t1, v1)
  
  p = (p1+p2)/2
  error = np.linalg.norm(p1-p2)**2
  
  return p, error