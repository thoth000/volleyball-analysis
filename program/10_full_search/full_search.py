import glob
import json
import numpy as np
import calibrate
import coord


# カメラデータ
cMat_c1, dist_c1, rotMat_c1, transVec_c1, dirVec_c1 = calibrate.getC1Data()
cMat_c2, dist_c2, rotMat_c2, transVec_c2, dirVec_c2 = calibrate.getC2Data()

# jsonファイルディレクトリ
c1Dir = "../../data/tracking/01_camera1/jsons"
c2Dir = "../../data/tracking/01_camera2/jsons"

# jsonファイル
c1Files = glob.glob(c1Dir + "/*.json")
c2Files = glob.glob(c2Dir + "/*.json")

samples = len(c1Files)
digit = len(str(samples))

for index in samples:
  c1File = open(c1Files[index], "r")
  c2File = open(c2Files[index], "r")
  
  c1Data = json.load(c1File)
  c2Data = json.load(c2File)
  
  searchResults = []