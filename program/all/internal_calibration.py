import cv2
import numpy as np
import glob

class InternalCalibration:
    def __init__(self, img_dir, squareX, squareY, squareSize):
        self.img_dir = img_dir
        self.number_of_squares_X = squareX
        self.number_of_squares_Y = squareY
        self.nX = self.number_of_squares_X - 1
        self.nY = self.number_of_squares_Y - 1
        self.square_size = squareSize

        self.object_points = []
        self.image_points  = []

        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        self.object_points_3D = np.zeros((self.nX * self.nY, 3), np.float32)
        self.object_points_3D = self.object_points_3D * self.square_size
    
    def calibrate(self):
        # 較正用の画像ファイルパス配列
        images = glob.glob(f"{self.img_dir}/*.png")

        for image_file in images:
            image = cv2.imread(image_file)  

        # グレースケールに変更
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
        # チェスボードの内角検知
        success, corners = cv2.findChessboardCorners(gray, (self.nY, self.nX), None)
     
        # 検知出来たらアルゴリズムを進める
        if success == True:
            # 3次元点の追加
            self.object_points.append(self.object_points_3D)
 
            # 小数までピクセルを求める（探索条件はcriteria）     
            corners_2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), self.criteria)       
       
            # 2次元点の追加
            self.image_points.append(corners_2)

        # カメラキャリブレーションを行う
        # ret : , mtx : , dist : ,
        # rvecs : , tvecs : 
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
            self.object_points, self.image_points, 
            gray.shape[::-1], None, None)
 
        # 画像寸法
        height, width = distorted_image.shape[:2]
        print(height, width)
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