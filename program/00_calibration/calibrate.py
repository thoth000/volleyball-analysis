import cv2
import numpy as np
import glob
 
# 補正画像パス関連
img_dir = "./iPhone_image"
file_name = "5.png"
distorted_img_filename = f"{img_dir}/resize/{file_name}" # 補正画像パス
 
# チェスボード
number_of_squares_X = 10 # X軸に沿ったチェス盤のマス目数
number_of_squares_Y = 7  # Y軸に沿ったチェス盤のマス目数
nX = number_of_squares_X - 1 # X軸に沿った内角の数
nY = number_of_squares_Y - 1 # X軸に沿った内角の数
square_size = 0.024 # 正方形辺長(単位 m)

# すべてのチェスボード画像（ワールド座標系）の3次元点のベクトルを格納する
object_points = []

# すべてのチェスボード画像（カメラ座標系）の2次元点のベクトルを格納する
image_points = []

# 終了基準の設定
# 特定の精度の達成、または反復上限に達したときに終了
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 3次元座標系における点の実世界座標の定義
# (Y, X, 0) = (0,0,0), (1,0,0), (2,0,0) ...., (6,9,0)
object_points_3D = np.zeros((nX * nY, 3), np.float32)       

object_points_3D[:,:2] = np.mgrid[0:nY, 0:nX].T.reshape(-1, 2) 
# 正方形辺長の実寸をかけて座標をm単位に変更
object_points_3D = object_points_3D * square_size

def main():
  img_dir = "./iPhone_image"
  # 較正用の画像ファイルパス配列
  images = glob.glob(f"{img_dir}/resize/*.png")

  for image_file in images:
    image = cv2.imread(image_file)  

    # グレースケールに変更
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
 
    # チェスボードの内角検知
    success, corners = cv2.findChessboardCorners(gray, (nY, nX), None)
     
    # 検知出来たらアルゴリズムを進める
    if success == True:
      # 3次元点の追加
      object_points.append(object_points_3D)
 
      # 小数までピクセルを求める（探索条件はcriteria）     
      corners_2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)       
       
      # 2次元点の追加
      image_points.append(corners_2)

      # チェスボードの内角描画
      # cv2.drawChessboardCorners(image, (nY, nX), corners_2, success)
                                                                                                                     
  # 目的画像の補正(カメラキャリブレーション)

  distorted_image = cv2.imread(distorted_img_filename)
  # カメラキャリブレーションを行う
  # ret : , mtx : , dist : ,
  # rvecs : , tvecs : 
  ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points, 
                                                    image_points, 
                                                    gray.shape[::-1], 
                                                    None, 
                                                    None)
 
  # 画像寸法
  height, width = distorted_image.shape[:2]
     
  # カメラ行列の絞り込み
  # 最適なカメラ行列を矩形の影響領域を返す
  optimal_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, 
                                                            (width,height), 
                                                            1, 
                                                            (width,height))
 
  # 画像補正
  undistorted_image = cv2.undistort(distorted_image, mtx, dist, None, 
                                    optimal_camera_matrix)
   
  # 画像のトリミング
  # 補正後に画像端に発生する黒領域を消去する
  # x, y, w, h = roi
  # undistorted_image = undistorted_image[y:y+h, x:x+w]

  # カメラキャリブレーションの主要パラメータ出力
  print("Optimal Camera matrix:") 
  print(optimal_camera_matrix) 

  print("\n Distortion coefficient:") 
  print(dist)

  print("\n Rotation Vectors:") 
  print(rvecs)
   
  print("\n Translation Vectors:") 
  print(tvecs) 
 
  # 補正画像の保存
  new_filename = f"{img_dir}/undistort/{file_name}"
  cv2.imwrite(new_filename, undistorted_image)

  cv2.destroyAllWindows()
     
main()