import cv2
import numpy as np
import glob

##############################################

def getObjectPoints(square_size, nX, nY):
  object_points = np.zeros((nX * nY, 3), np.float32)       
  object_points[:,:2] = np.mgrid[0:nY, 0:nX].T.reshape(-1, 2) 
  # 正方形辺長の実寸をかけて座標をmm単位に変更
  object_points = object_points * square_size
  return object_points

def getImagePoints(image_file, nX, nY):
  image = cv2.imread(image_file)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
  # チェスボードの内角検知
  success, corners = cv2.findChessboardCorners(gray, (nY, nX), None)
  if success == True:
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners_2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
    return True, corners_2
  else:
    return False, []

def calibration(calib_dir, number_of_squares_X = 10, number_of_squares_Y = 7, square_size = 24, img_width = 1920, img_height = 1080):
  image_files = glob.glob(f"{calib_dir}/*.png")

  nX = number_of_squares_X - 1
  nY = number_of_squares_Y - 1
  
  object_points = getObjectPoints(square_size, nX, nY)

  object_points_list = []
  image_points_list = []

  for image_file in image_files:
    ret, image_points = getImagePoints(image_file, nX, nY)
    if ret:
      object_points_list.append(object_points)
      image_points_list.append(image_points)
  
  ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points_list, 
                                                    image_points_list, 
                                                    (img_width, img_height), 
                                                    None,
                                                    None)
  
  optimal_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, 
                                                            (img_width, img_height), 
                                                            1, 
                                                            (img_width, img_height))

  return mtx, optimal_camera_matrix, dist