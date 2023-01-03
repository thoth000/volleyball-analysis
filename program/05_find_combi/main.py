import numpy as np
import cv2
import csv
import json
import glob
from find_conbi import *
from structure import ErrorValue

# maximum error limit
errorLimit = 200000

# camera1 data file
c1_dir      = "data_camera1"
cMat_c1     = np.loadtxt("{}/camera_mat.csv".format(c1_dir), delimiter=",")
dist_c1     = np.loadtxt("{}/dist.csv".format(c1_dir), delimiter=",")
rotMat_c1   = np.loadtxt("{}/rotation_mat.csv".format(c1_dir), delimiter=",")
transVec_c1 = np.loadtxt("{}/trans_vec.csv".format(c1_dir), delimiter=",")
dirVec_c1   = np.loadtxt("{}/dir_vec.csv".format(c1_dir), delimiter=",")

# camera2 data file
c2_dir      = "data_camera2"
cMat_c2     = np.loadtxt("{}/camera_mat.csv".format(c2_dir), delimiter=",")
dist_c2     = np.loadtxt("{}/dist.csv".format(c2_dir), delimiter=",")
rotMat_c2   = np.loadtxt("{}/rotation_mat.csv".format(c2_dir), delimiter=",")
transVec_c2 = np.loadtxt("{}/trans_vec.csv".format(c2_dir), delimiter=",")
dirVec_c2   = np.loadtxt("{}/dir_vec.csv".format(c2_dir), delimiter=",")

# open file
c1File = open("c1.json", "r")
c2File = open("c2.json", "r")

# load json
c1Data = json.load(c1File)
c2Data = json.load(c2File)

# close file
c1File.close()
c2File.close()

# list for output of function "getErrorValue"
results = []

for id1 in c1Data:
  c1Coord = np.array(c1Data[id1], dtype=np.float32)
  vec_c1  = getHeadingVector(c1Coord, cMat_c1, rotMat_c1)
  for id2 in c2Data:
    c2Coord = np.array(c2Data[id2], dtype=np.float32)
    vec_c2  = getHeadingVector(c2Coord, cMat_c2, rotMat_c2)
    
    error, worldCoord = getErrorValue(transVec_c1, vec_c1, transVec_c2, vec_c2)
    
    squaredError = ErrorValue(id1, id2, error, worldCoord)
    results.append(squaredError)
    
sorted_results = sorted(results, key=lambda obj: obj.error)

correspondDict = {}

for result in sorted_results:
  id1   = result.id1
  id2   = result.id2
  error = result.error
  
  if error > errorLimit:
    break
  
  if id1 in correspondDict.keys():
    continue
  
  if id2 in correspondDict.values():
    continue
  
  correspondDict[id1] = id2
  print(id1, id2, error)

with open("output.json", "w") as f:
  json.dump(correspondDict, f)