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

        self.object_points_3D = np.zeros((nX * nY, 3), np.float32)
        self.object_points_3D = self.object_points_3D * self.square_size
    
    def calibrate():
        # main関数書き換え