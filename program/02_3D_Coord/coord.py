import numpy as np
import sympy

width  = 1920
height = 1080

def getHeadingVector(coord, cameraMat, rotationMat):
    u = coord[0]
    v = coord[1]
    # カメラ座標系での投影面上ポイント
    xC = u - width/2
    yC = v - height/2
    zC = (cameraMat[0, 0] + cameraMat[1, 1])/2 # x, y向き焦点距離の中間値

    # カメラ座標系でのポイント位置ベクトル
    vecC = np.float32([xC, yC, zC])

    # 実空間座標系での方向ベクトルに変換
    vecW = np.dot(rotationMat, vecC) * (-1)

    # 正規化
    vecW /= np.linalg.norm(vecW)

    return vecW

def computeClosestPoint(t1, v1, t2, v2):
  # 分子
  # v1, v2が単位ベクトル化されてないならコメント外す
  v1 = v1 / np.linalg.norm(v1)
  v2 = v2 / np.linalg.norm(v2)
  
  part0 = v1 - (np.dot(v2, v1) * v2)
  part1 = t2 - t1
  numerator = np.dot(part0, part1)
  
  # 分母
  denominator = 1 - (np.dot(v2, v1))**2
  
  point = t1 + (numerator/denominator) * v1
  return point

# 2直線の中点と最近点同士の誤差を返す(main関数で実行)
def compute3dCoord(t1, v1, t2, v2):
  # 最近点
  p1 = computeClosestPoint(t1, v1, t2, v2)
  p2 = computeClosestPoint(t2, v2, t1, v1)
  
  p = (p1+p2)/2
  
  return p