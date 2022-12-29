import numpy as np
import cv2
import csv
import json
import glob
from coord import *

# camera1 - camera2 ID対応JSON
correspondFile  = open("correspond.json", "r")

# data

c1Files = glob.glob("c1_json/*.json")
c2Files = glob.glob("c2_json/*.json")
jsonDataNum = min(len(c1Files), len(c2Files))
correspondData  = json.load(correspondFile)

digit = len(str(jsonDataNum))

# camera1 data file
c1_dir      = "../01_camera_position/data_camera1"
cMat_c1     = np.loadtxt("{}/camera_mat.csv".format(c1_dir), delimiter=",")
dist_c1     = np.loadtxt("{}/dist.csv".format(c1_dir), delimiter=",")
rotMat_c1   = np.loadtxt("{}/rotation_mat.csv".format(c1_dir), delimiter=",")
transVec_c1 = np.loadtxt("{}/trans_vec.csv".format(c1_dir), delimiter=",")
dirVec_c1   = np.loadtxt("{}/dir_vec.csv".format(c1_dir), delimiter=",")

# camera2 data file
c2_dir      = "../01_camera_position/data_camera2"
cMat_c2     = np.loadtxt("{}/camera_mat.csv".format(c2_dir), delimiter=",")
dist_c2     = np.loadtxt("{}/dist.csv".format(c2_dir), delimiter=",")
rotMat_c2   = np.loadtxt("{}/rotation_mat.csv".format(c2_dir), delimiter=",")
transVec_c2 = np.loadtxt("{}/trans_vec.csv".format(c2_dir), delimiter=",")
dirVec_c2   = np.loadtxt("{}/dir_vec.csv".format(c2_dir), delimiter=",")

for i in range(jsonDataNum):
  oldJsonName = "{}.json".format(i)
  
  c1File = open("c1_json/{}".format(oldJsonName), "r")
  c2File = open("c2_json/{}".format(oldJsonName), "r")
  
  c1Data = json.load(c1File)
  c2Data = json.load(c2File)

  coordData = {}
  
  for playerId in c1Data:
    if playerId in correspondData:
      correspondId = correspondData[playerId]
    else:
      continue
    
    if not correspondId in c2Data:
      continue
    
    c1Coord = np.array(c1Data[playerId],     dtype = np.float32)
    c2Coord = np.array(c2Data[correspondId], dtype = np.float32)
    
    #c1UndistortedCoord = cv2.undistortPoints(src = c1Coord, cameraMatrix = cMat_c1, distCoeffs = dist_c1).reshape(-1)
    #c2UndistortedCoord = cv2.undistortPoints(src = c2Coord, cameraMatrix = cMat_c2, distCoeffs = dist_c2).reshape(-1)
    
    #vec_c1 = getHeadingVector(c1UndistortedCoord, cMat_c1, rotMat_c1)
    #vec_c2 = getHeadingVector(c2UndistortedCoord, cMat_c2, rotMat_c2)
    
    vec_c1 = getHeadingVector(c1Coord, cMat_c1, rotMat_c1)
    vec_c2 = getHeadingVector(c2Coord, cMat_c2, rotMat_c2)
    
    worldCoord = compute3dCoord(transVec_c1, vec_c1, transVec_c2, vec_c2)
    
    coordData[playerId] = worldCoord.tolist()

  newJsonName = "{}.json".format(str(i).zfill(digit))

  with open("output/{}".format(newJsonName), "w") as f:
    json.dump(coordData, f)

  print("write data in {}".format(newJsonName))

  c1File.close()
  c2File.close()

correspondFile.close()
