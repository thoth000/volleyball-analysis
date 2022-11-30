import csv
import numpy as np

OUTPUT_FILE = "./data/output.csv"
IMG_WIDTH = 1920
IMG_HEIGHT = 1080

netHeightDict = {
    "小学生" : 2000,
    "中学生男子" : 2300,
    "高校生男子" : 2400,
    "一般男子" : 2430,
    "中学生女子" : 2150,
    "高校生女子" : 2200,
    "一般女子" : 2240
}
netHeight = netHeightDict["一般男子"]

objectDict = [
    # コート原点から長辺を回る向き
    [0, 0, 0],
    [6000, 0, 0],
    [9000, 0, 0],
    [12000, 0, 0],
    [18000, 0, 0],
    [18000, 9000, 0],
    [12000, 9000, 0],
    [9000, 9000, 0],
    [6000, 9000, 0],
    [0, 9000, 0],
    # ネット原点側（下、上、アンテナ先）、逆側（下、上、アンテナ先）
    [9000, 0, netHeight - 1000],
    [9000, 0, netHeight],
    [9000, 0, netHeight + 800],
    [9000, 9000, netHeight - 1000],
    [9000, 9000, netHeight],
    [9000, 9000, netHeight + 800]
]

objectPoints = [
    objectDict[0],
    objectDict[1],
    objectDict[2],
    objectDict[3],
    objectDict[4],  
    objectDict[5],
    objectDict[6],
    objectDict[7],
    objectDict[8],
    objectDict[11],
    objectDict[12],
    objectDict[14],
    objectDict[15]
]

def getCoordCSV(fileName):
    table = []
    file = open(fileName, "r")
    reader = csv.reader(file)
    for row in reader:
        table.append(list(map(float, row)))
    file.close()
    return table

def getObjectPointFromIndexList(indexList):
    retList = []
    for index in indexList:
        retList.append(objectDict[index])
    return retList

def writeCameraInfoCSV(cMat, dist, rotMat, tvec, rvec, csvFileName = "./data/cameraInfo.csv"):
    with open(csvFileName, mode="w") as csvFile:
        np.savetxt(csvFile, cMat,   delimiter=',')
        np.savetxt(csvFile, dist,   delimiter=',')
        np.savetxt(csvFile, rotMat, delimiter=',')
        np.savetxt(csvFile, tvec,   delimiter=',')
        np.savetxt(csvFile, rvec,   delimiter=",")
        
if __name__ == "__main__":
    print(getCoordCSV(OUTPUT_FILE))