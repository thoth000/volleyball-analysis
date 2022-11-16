import numpy as np
import cv2
import csv
import sys

import calibration
import plot_image
from external_parameter import *
from utility import *

### 宣言部
calib_dir = "../00_calibration/iPhone_image/resize"
image_path = "./image/target.png"

imagePoints = []

if __name__ == "__main__":
    # コマンドライン引数
    argv = sys.argv
    # カメラ内部パラメータ取得
    cameraMatrix, optimalCameraMatrix, dist = calibration.calibration(calib_dir)
    print("[完了] カメラ内部パラメータ取得")
    # 画像読み込み
    image = cv2.imread(image_path)
    und_image = cv2.undistort(image, cameraMatrix, dist, None, optimalCameraMatrix)
    print("[完了] 較正用画像読み込み")

    if (len(argv) > 1) and (argv[1] == "click"):
        # 画像座標出力先ファイルの初期化
        output_file = open(OUTPUT_FILE, "w")
        output_file.close()
        # 画像座標書き込み
        plot_image.getImagePoints(und_image, True)
        print("[完了] クリックによる画像座標書き込み")
    else:
        print("[SKIP] クリックによる画像座標書き込み")
    # 画像座標読み込み
    imagePoints = getCoordCSV(OUTPUT_FILE)
    print("[完了] 画像座標読み込み")
    # カメラ外部パラメータ取得
    objectPoints = np.array(objectPoints, dtype=np.float32)
    imagePoints = np.array(imagePoints, dtype=np.float32)
    #R_raw, t_raw, rvec, tvec = externalParameter(cameraMatrix, dist, objectPoints, imagePoints)
    R_raw, t_raw, rvec, tvec = externalParameter(optimalCameraMatrix, dist, objectPoints, imagePoints)
    print("[完了] カメラ外部パラメータ取得")
    print("R_raw\n", R_raw, "\n")
    print("t_raw\n", t_raw, "\n")
