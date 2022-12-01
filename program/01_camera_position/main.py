import numpy as np
import cv2
import csv
import sys

import calibration
import plot_image
from external_parameter import *
from utility import *

### 宣言部
calib_dir = "../utility/calib_images"
image_path = "./image/target.png"

imagePoints = []
pointIndexList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15]

if __name__ == "__main__":
    # コマンドライン引数
    argv = sys.argv
    
    # カメラ内部パラメータ取得
    cameraMatrix, optimalCameraMatrix, dist = calibration.calibration(calib_dir)
    print("[完了] カメラ内部パラメータ取得")
    print("内部パラメータ\n", cameraMatrix, "\n")
    
    # 画像読み込み
    image = cv2.imread(image_path)
    print("[完了] 較正用画像読み込み")

    # 画像座標書き込み
    if (len(argv) > 1) and (argv[1] == "click"):
        # ポイントの指定
        print("[入力]画像クリックポイントの指定")
        pointIndexList = list(map(int, input().split()))
        
        # 画像座標出力先ファイルの初期化
        output_file = open(OUTPUT_FILE, "w")
        output_file.close()
        
        # 画像クリックによるCSV書き込み
        plot_image.getImagePoints(image, True)
        print("[完了] クリックによる画像座標書き込み")
    else:
        print("[SKIP] クリックによる画像座標書き込み")
    
    # 画像座標読み込み
    imagePoints = getCoordCSV(OUTPUT_FILE)
    print("[完了] 画像座標読み込み")
    
    # カメラ外部パラメータ取得
    objectPoints = np.array(getObjectPointFromIndexList(pointIndexList), dtype=np.float32)
    imagePoints = np.array(imagePoints, dtype=np.float32)
    
    camera2worldRotMat, cameraPosition = externalParameter(cameraMatrix, dist, objectPoints, imagePoints)
    #R_raw, t_raw, rvec, tvec = externalParameter(optimalCameraMatrix, dist, objectPoints, imagePoints)
    cameraPosition = cameraPosition.reshape(-1)

    # カメラの単位方向ベクトル
    cameraDirection = np.dot(camera2worldRotMat, [0, 0, 1]) * (-1)

    print("[完了] カメラ外部パラメータ取得\n")
    print("カメラ座標系→世界座標系の回転行列\n", camera2worldRotMat, "\n")
    print("世界座標系のカメラ位置\n",           cameraPosition,     "\n")
    print("世界座標系のカメラ方向ベクトル\n",    cameraDirection,    "\n")
    
    # CSV書き込み
    writeCameraInfoCSV(cameraMatrix, dist, camera2worldRotMat, cameraPosition, cameraDirection)