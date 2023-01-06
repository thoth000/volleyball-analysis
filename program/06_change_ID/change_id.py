import glob
import os
import json

# ---関数定義---

def createMatchedDict(dictData):
  retDict = {}
  for key in dictData:
    retDict[key] = False
  
  return retDict

def getBoxCenter(array):
  x_lt = array[51]
  y_lt = array[52]

  x    = x_lt + array[53]/2
  y    = y_lt + array[54]/2
  return [x, y]

def calculateError(oldID, p1, newID, p2):
  error = (p1[0] - p2[0])**2 + \
          (p1[1] - p2[1])**2
  
  return [error, oldID, newID]

# ---関数定義終了---

originDir = "./origin_c2"
outDir    = "./track_c2"

# 出力ディレクトリ作成
os.makedirs(outDir, exist_ok=True)

currentIDcorrespondence = {} # 現ID : 元IDの対応表
position = {}

# ファイル群の取り出し
files = glob.glob(originDir + "/*.json")
digit = len(str(len(files)))

# 初期処理(ID対応付)
with open(files[0], "r") as file:
  dictData = json.load(file)
  for key in dictData:
    currentIDcorrespondence[key] = key
    position[key] = getBoxCenter(dictData[key])

# フレームごとの処理
for fileIndex, path in enumerate(files):
  file = open(path, "r")
  dictData = json.load(file)
  matchedDict = createMatchedDict(currentIDcorrespondence)
  
  unmatchedOldIDs = []
  unmatchedNewIDs = []
  # 未対応IDの特定
  for idx in dictData:
    if idx in currentIDcorrespondence.keys():
      position[idx] = getBoxCenter(dictData[idx]) # 位置の更新
      matchedDict[idx] = True
    else:
      unmatchedNewIDs.append(idx)
  
  for idx in matchedDict:
    if not matchedDict[idx]: # 未対応のIDなら
      unmatchedOldIDs.append(idx)
  
  # ---対応付け---
  errorList = []
  # 全探索
  for oldID in unmatchedOldIDs:
    for newID in unmatchedNewIDs:
      errorData = calculateError( \
        oldID, position[oldID], \
        newID, dictData[newID], \
      )
      errorList.append(errorData)
  errorList.sort()

  index = 0
  while((len(unmatchedOldIDs) > 0) and (len(unmatchedNewIDs) > 0)):
    data = errorList[index]
    error = data[0]
    oldID = data[1]
    newID = data[2]

    index += 1 # indexを進める
    # IDが配列に含まれていないならスルー
    if not((oldID in unmatchedOldIDs) and (newID in unmatchedNewIDs)):
      continue
    
    # 未対応IDリストからの削除
    unmatchedOldIDs.remove(oldID)
    unmatchedNewIDs.remove(newID)
    # 元IDの引継ぎ
    originID = currentIDcorrespondence[oldID] # 元ID
    currentIDcorrespondence[newID] = originID
    position[newID] = getBoxCenter(dictData[newID]) # 位置の更新
    # 前IDのデータ消去
    currentIDcorrespondence.pop(oldID)
    position.pop(oldID)
    # 現フレームの出現IDに登録
    matchedDict[newID] = True

  # 新規IDと対応付ける旧IDがなくなった場合
  if len(unmatchedOldIDs) == 0:
    for newID in unmatchedNewIDs:
      # 新規IDの登録
      currentIDcorrespondence[newID] = newID
      position[newID] = getBoxCenter(dictData[newID])
      # 現フレームの出現IDに登録
      matchedDict[newID] = True

  # ---対応付け終了---
  # ---出力部---
  outDict = {}

  for currentID in position:
    if not(matchedDict[currentID]):
      print(currentID)
      continue

    originID = currentIDcorrespondence[currentID]
    coord    = position[currentID] # 出力するのがboxの中点座標です！！！

    outDict[originID] = coord

  outPath = outDir + "/" + str(fileIndex).zfill(digit) + ".json"
    
  with open(outPath, "w") as outFile:
    json.dump(outDict, outFile, indent=4)

  # ---出力部終了---
  file.close()
  print("created", outPath)