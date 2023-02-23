import glob
import json
import numpy as np
import os
import calibrate
import coord

# カメラデータ
cMat_c1, dist_c1, rotMat_c1, transVec_c1, dirVec_c1 = calibrate.getC1Data()
cMat_c2, dist_c2, rotMat_c2, transVec_c2, dirVec_c2 = calibrate.getC2Data()

# jsonファイルディレクトリ
# c1Dir = "../../data/tracking/01_camera1/jsons"
# c2Dir = "../../data/tracking/01_camera2/jsons"
c1Dir = "../../data/undistort_showbox/01_camera1/jsons"
c2Dir = "../../data/undistort_showbox/01_camera2/jsons"

# jsonファイル
c1Files = glob.glob(c1Dir + "/*.json")
c2Files = glob.glob(c2Dir + "/*.json")

samples = len(c1Files)
digit = len(str(samples))

zMaxLimit = 1000
zMinLimit = -300

# 許容距離
errorLimit = 2000

# データ出力先
outputDir = "output"
os.makedirs(outputDir, exist_ok=True)

# 誤差出力先
subOutDir = "sub"
os.makedirs(subOutDir, exist_ok=True)

# フレーム処理
for index in range(samples):
  # 進捗表示
  print("processing", index)
  # フレームデータ出力先
  outputPath = outputDir + "/{}.json".format(str(index).zfill(digit))
  
  c1File = open(c1Files[index], "r")
  c2File = open(c2Files[index], "r")
  
  c1Data = json.load(c1File)
  c2Data = json.load(c2File)
  
  searchResults = []
  # 全探索
  for id1 in c1Data:
    # coord1 = coord.getHipCoord(c1Data[id1])
    coord1 = coord.getBoxCenter(c1Data[id1])
    vec1 = coord.getHeadingVector(coord1, cMat_c1, rotMat_c1)
    for id2 in c2Data:
      # coord2 = coord.getHipCoord(c2Data[id2])
      coord2 = coord.getBoxCenter(c2Data[id2])
      vec2 = coord.getHeadingVector(coord2, cMat_c2, rotMat_c2)
      
      coord3D, error, coord3D_L1, coord3D_L2 = coord.getClosestPoint(transVec_c1, vec1, transVec_c2, vec2)
      
      # if error > errorLimit:
      #  continue

      subData = {
        "x1" : coord3D_L1[0],
        "y1" : coord3D_L1[1],
        "z1" : coord3D_L1[2],
        "x2" : coord3D_L2[0],
        "y2" : coord3D_L2[1],
        "z2" : coord3D_L2[2],
      }
      
      data = {
        "position_x":coord3D[0],
        "position_y":coord3D[1],
        "position_z":coord3D[2],
        "c1_id":id1,
        "c2_id":id2,
        "error":error,
        "data" : subData
      }
      searchResults.append(data)
  
  searchResults = sorted(searchResults, key=lambda d: d["error"])
  
  # 誤差確認用出力プログラム
  subOutPath = subOutDir + "/{}.json".format(str(index).zfill(digit))
  with open(subOutPath, "w") as subOutFile:
    json.dump(searchResults, subOutFile, indent=4)
  
  idList1 = list(c1Data.keys())
  idList2 = list(c2Data.keys())
  
  personIndex = 1
  outputData = {}
  while ((len(idList1) > 0) and (len(idList2) > 0) and (len(searchResults) > 0)):
    data = searchResults.pop(0)

    if not((data["c1_id"] in idList1) and (data["c2_id"] in idList2)):
      continue

    if (data["position_z"] > zMaxLimit) or (data["position_z"] < zMinLimit):
      continue

    outputData[str(personIndex)] = data
    idList1.remove(data["c1_id"])
    idList2.remove(data["c2_id"])
    personIndex += 1
  
  # データ出力
  with open(outputPath, "w") as outputFile:
    json.dump(outputData, outputFile, indent=4)
