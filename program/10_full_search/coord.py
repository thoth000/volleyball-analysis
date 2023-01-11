import numpy as np

# 検知枠の中心座標(画像座標)
def getBoxCenter(array):
  x = array[51] + array[53]/2
  y = array[52] + array[54]/2
  
  return np.array([x, y])

# keypointsから腰座標(画像座標)
def getHipCoord(array):
  left  = np.array(array[11*3: 11*3+2])
  right = np.array(array[12*3: 12*3+2])
  
  ret = (left+right)/2
  return ret

# 画像座標→カメラ座標系→実空間座標系
def getHeadingVector(coord, cameraMat, rotationMat, imgWidth=1920, imgHeight=1080):
    u = coord[0]
    v = coord[1]
    # カメラ座標系での投影面上ポイント
    xC = u - imgWidth/2
    yC = v - imgHeight/2
    zC = (cameraMat[0, 0] + cameraMat[1, 1])/2 # x, y向き焦点距離の中間値

    # カメラ座標系でのポイント位置ベクトル
    vecC = np.float32([xC, yC, zC])

    # 実空間座標系での方向ベクトルに変換
    vecW = np.dot(rotationMat, vecC) * (-1)

    # 正規化
    vecW /= np.linalg.norm(vecW)
    return vecW

# 直線上の最近点を求める
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
def getClosestPoint(t1, v1, t2, v2):
  # 最近点
  p1 = computeClosestPoint(t1, v1, t2, v2)
  p2 = computeClosestPoint(t2, v2, t1, v1)
  
  p = (p1+p2)/2
  error = np.linalg.norm(p1-p2)
  
  return p, error, p1, p2