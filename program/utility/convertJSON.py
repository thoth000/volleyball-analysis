# AlphaPose生成JSON変換プログラム
import json

end_index = 275

image_range = ["{}.jpg".format(i) for i in range(0, end_index + 1)]

with open("json_data/c1.json") as c1File:
    c1Data = c1File

with open("json_data/c2.json") as c2File:
    c2Data = c2File

for imgIndex in image_range:
    c1TmpData = {}
    c2TmpData = {}
    while (True): # c1 roop
        if len(c1Data) == 0:
            break

        tmpData = c1Data.pop(0)
        if tmpData["image_id"] != imgIndex:
            tmpData.insert(0, tmpData)
            break

        ExtractedData = {
            "id" : int(float(tmpData.idx)),
            "coord" : tmpData.keypoints[]
        }
