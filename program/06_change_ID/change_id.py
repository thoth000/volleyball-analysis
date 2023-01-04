import glob
import os
import json

def createMatchedDict(dictData):
  retDict = {}
  for key in dictData:
    retDict[key] = False
  
  return retDict

originDir = "./origin_c1"

currentIDcorrespondence = {} # 現ID : 元IDの対応表
position = {}

files = glob.glob(originDir + "/*.json")

# 初期処理(ID対応付)
with open(files[0], "r") as file:
  dictData = json.load(file)
  for key in dictData:
    currentIDcorrespondence[key] = key
    position[key] = dictData[key]

for path in files:
  file = open(path, "r")
  dictData = json.load(file)
  matchedDict   = createMatchedDict(currentIDcorrespondence)
  
  unmatchedOldIDs = []
  unmatchedNewIDs = []
  # 未対応IDの特定
  for idx in dictData:
    if idx in currentIDcorrespondence.keys():
      position[idx] = dictData[idx]
      matchedDict[idx] = True
    else:
      unmatchedNewIDs.append(idx)
  
  for idx in matchedDict:
    if not matchedDict[idx]: # 未対応のIDなら
      unmatchedOldIDs.append(idx)

  