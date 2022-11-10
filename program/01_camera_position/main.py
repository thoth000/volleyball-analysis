import numpy as np
import cv2
import csv

import calibration
import plot_image
import external_parameter
from utility import *

### 宣言部
calib_dir = "../00_calibration/iPhone_image/resize"
image_path = "./image/target.png"
objectPoints = [
    [0, 0, 0],
    [900, 0, 0],
    [1800, 0, 0],
    [1800, 900, 0],
    [900, 900, 0],
    [0, 900, 0],
    [900, 450, 140]
]
imagePoints = []

### 処理部
# カメラ内部パラメータ取得
cameraMatrix, optimalCameraMatrix, dist = calibration.calibration(calib_dir)
# 画像読み込み
image = cv2.imread(image_path)
und_image = cv2.undistort(image, cameraMatrix, dist, None, optimalCameraMatrix)
# 画像座標出力先ファイルの初期化
output_file = open(OUTPUT_FILE, "w")
output_file.close()
# 画像座標書き込み
plot_image.getImagePoints(und_image, True)
# 画像座標読み込み
imagePoints = getCoordCSV(OUTPUT_FILE)
print(imagePoints)