import numpy as np

def getC1Data():
  c1_dir      = "../01_camera_position/data_camera1"
  cMat_c1     = np.loadtxt("{}/camera_mat.csv".format(c1_dir), delimiter=",")
  dist_c1     = np.loadtxt("{}/dist.csv".format(c1_dir), delimiter=",")
  rotMat_c1   = np.loadtxt("{}/rotation_mat.csv".format(c1_dir), delimiter=",")
  transVec_c1 = np.loadtxt("{}/trans_vec.csv".format(c1_dir), delimiter=",")
  dirVec_c1   = np.loadtxt("{}/dir_vec.csv".format(c1_dir), delimiter=",")
  
  return cMat_c1, dist_c1, rotMat_c1, transVec_c1, dirVec_c1

def getC2Data():
  c2_dir      = "../01_camera_position/data_camera2"
  cMat_c2     = np.loadtxt("{}/camera_mat.csv".format(c2_dir), delimiter=",")
  dist_c2     = np.loadtxt("{}/dist.csv".format(c2_dir), delimiter=",")
  rotMat_c2   = np.loadtxt("{}/rotation_mat.csv".format(c2_dir), delimiter=",")
  transVec_c2 = np.loadtxt("{}/trans_vec.csv".format(c2_dir), delimiter=",")
  dirVec_c2   = np.loadtxt("{}/dir_vec.csv".format(c2_dir), delimiter=",")
  
  return cMat_c2, dist_c2, rotMat_c2, transVec_c2, dirVec_c2
