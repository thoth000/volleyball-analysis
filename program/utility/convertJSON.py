# AlphaPose生成JSON変換プログラム
import json

end_index = 275

with open("json_data/c1.json") as c1File:
    c1Data = json.load(c1File)

with open("json_data/c2.json") as c2File:
    c2Data = json.load(c2File)

for i in range(0, end_index+1):
    imgIndex = "{}.jpg".format(i)
    
    c1TmpData = {}
    c2TmpData = {}
    while (True): # c1 roop
        if len(c1Data) == 0:
            break

        tmpData = c1Data.pop(0)
        
        if tmpData["image_id"] != imgIndex:
            c1Data.insert(0, tmpData)
            break
        
        leftHip  = tmpData["keypoints"][11*3 : 11*3+2]
        rightHip = tmpData["keypoints"][12*3 : 12*3+2]

        if (int(leftHip[0]) == 0) or (int(rightHip[0]) == 0):
            continue
        
        midHip   = [
            (leftHip[0] + rightHip[0]) / 2,
            (leftHip[1] + rightHip[1]) / 2
        ]
        
        playerId = int(float(tmpData["idx"]))
        
        c1TmpData[playerId] = midHip
    
    while (True): # c2 roop
        if len(c2Data) == 0:
            break

        tmpData = c2Data.pop(0)
        
        if tmpData["image_id"] != imgIndex:
            c2Data.insert(0, tmpData)
            break
        
        leftHip  = tmpData["keypoints"][11*3 : 11*3+2]
        rightHip = tmpData["keypoints"][12*3 : 12*3+2]
        
        if (int(leftHip[0]) == 0) or (int(rightHip[0]) == 0):
            continue
        
        midHip   = [
            (leftHip[0] + rightHip[0]) / 2,
            (leftHip[1] + rightHip[1]) / 2
        ]
        
        playerId = int(float(tmpData["idx"]))
        
        c2TmpData[playerId] = midHip
    
    outputFile = "{}.json".format(i)
    
    with open("c1_json/{}".format(outputFile), "w") as f:
        json.dump(c1TmpData, f)
        
    with open("c2_json/{}".format(outputFile), "w") as f:
        json.dump(c2TmpData, f)
