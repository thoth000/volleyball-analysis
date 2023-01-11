import os
import json

def getMovieFrame(path):
  index = 0
  with open(path, "r") as file:
    datas = json.load(file)
    # 最後尾のデータ取り出し
    image_id = datas[-1]["image_id"] # "275.png"
    index_str = image_id[:-4] # "275"
    index     = int(index_str)

  # 0-indexed, so plus 1.
  return index + 1


def splitJson(path, outDir, digit):
  os.makedirs(outDir, exist_ok=True)

  with open(path, "r") as file:
    datas = json.load(file)
    # 初期処理
    frameDict = {}
    
    image_id  = datas[0]["image_id"]
    index_str = image_id[:-4]
    outPath   = outDir + "/" + index_str.zfill(digit) + ".json"
    
    outFile   = open(outPath, "w")
    
    for data in datas:
      if data["image_id"] != image_id:
        json.dump(frameDict, outFile, indent=4)
        outFile.close()
        
        frameDict = {}
        
        image_id  = data["image_id"]
        index_str = image_id[:-4]
        outPath   = outDir + "/" + index_str.zfill(digit) + ".json"
        
        outFile = open(outPath, "w")
      # 欲しいデータ
      idx = str(int(data["idx"]))
      keypoints = data["keypoints"]
      box       = data["box"]
      # boxのデータ形式
      # [x_leftTop, y_leftTop, width, height]
      frameDict[idx] = keypoints + box
    
    json.dump(frameDict, outFile, indent=4)
    outFile.close()
  print("created", outDir)


# 出力ディレクトリの作成
os.makedirs("origin_c1", exist_ok=True)

os.makedirs("origin_c2", exist_ok=True)

# c1_path = "../../data/tracking/01_camera1/alphapose-results.json"
# c2_path = "../../data/tracking/01_camera2/alphapose-results.json"

c1_path = "../../data/undistort_showbox/01_camera1/alphapose-results.json"
c2_path = "../../data/undistort_showbox/01_camera2/alphapose-results.json"

frames = getMovieFrame(c1_path)
digit  = len(str(frames))

splitJson(c1_path, "origin_c1", digit)
splitJson(c2_path, "origin_c2", digit)