import numpy as np

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

p = np.array([0, 9000, 0])

t = np.loadtxt("../../data/calibration/trans_vec.csv", delimiter=",")

tmpVec = p - t
# 正解の単位ベクトル
correct = tmpVec / np.linalg.norm(tmpVec)

# カメラ行列
camMat = np.loadtxt("../../data/calibration/camera_mat.csv", delimiter=",")
# 回転行列
rotMat = np.loadtxt("../../data/calibration/rotation_mat.csv", delimiter=",")

# 元動画
originCoord = [813, 1056]
origin = getHeadingVector(originCoord, camMat, rotMat)
print(np.linalg.norm(origin - correct))

# 歪みノーマル
normalCoord = [815, 1050]
normal = getHeadingVector(normalCoord, camMat, rotMat)
print(np.linalg.norm(normal - correct))

# 歪み新
newCoord = [815, 1049]
new = getHeadingVector(newCoord, camMat, rotMat)
print(np.linalg.norm(new - correct))
