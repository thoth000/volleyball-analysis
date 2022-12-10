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

def compute3dCoord(t1, v1, t2, v2):
    # 媒介変数2種
    h = sympy.Symbol("h")
    s = sympy.Symbol("s")

    # 距離二乗和関数
    R = ((t1[0] + h*v1[0]) - (t2[0] + s*v2[0]))**2 + \
        ((t1[1] + h*v1[1]) - (t2[1] + s*v2[1]))**2 + \
        ((t1[2] + h*v1[2]) - (t2[2] + s*v2[2]))**2
    
    # 偏微分
    dR_dh = sympy.diff(R, h)
    dR_ds = sympy.diff(R, s)

    # 極小値を求める
    result = sympy.solve([dR_dh, dR_ds])
    h_val = result[h]
    s_val = result[s]

    # 二乗和誤差の出力
    # error = ((t1[0] + h_val*v1[0]) - (t2[0] + s_val*v2[0]))**2 + \
    #         ((t1[1] + h_val*v1[1]) - (t2[1] + s_val*v2[1]))**2 + \
    #         ((t1[2] + h_val*v1[2]) - (t2[2] + s_val*v2[2]))**2
    # print("error :", error, "\n")

    # 2直線上の最近点
    closePoint1 = np.float32([
        t1[0] + h_val * v1[0],
        t1[1] + h_val * v1[1],
        t1[2] + h_val * v1[2],
    ])
    closePoint2 = np.float32([
        t2[0] + s_val * v2[0],
        t2[1] + s_val * v2[1],
        t2[2] + s_val * v2[2],
    ])

    # 推定3次元ポイント
    targetPoint = (closePoint1 + closePoint2)/2
    return targetPoint