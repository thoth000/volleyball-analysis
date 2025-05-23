import cv2
import numpy as np
import math
# カメラ外部パラメータを求める
# cameraMatrix : カメラ行列(fx, fy, cx, cyが入ってる)
# distCoef     : 歪みベクトル
# objectPoints : 実空間座標(3次元)
# imagePoints  : 画像座標(2次元)
def externalParameter(cameraMatrix, distCoef, points3D, points2D):
    ret, rvec, tvec = cv2.solvePnP(points3D, points2D, cameraMatrix, distCoef)

    # R_mat : 回転行列(world -> camera)
    # R_raw : 回転行列(camera -> world)
    R_mat, _ = cv2.Rodrigues(rvec)
    R_raw = R_mat.T
    # t_raw : カメラ位置ベクトル
    t_raw = -R_raw @ tvec
    t_raw = t_raw.reshape(1, 3)

    return R_raw, t_raw