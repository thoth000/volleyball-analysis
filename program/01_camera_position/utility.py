import csv
OUTPUT_FILE = "./data/output.csv"

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

objectDict = {
    # コート原点から長辺を回る向き
    "CP0" : [0, 0, 0],
    "CP1" : [6000, 0, 0],
    "CP2" : [9000, 0, 0],
    "CP3" : [12000, 0, 0],
    "CP4" : [18000, 0, 0],
    "CP5" : [18000, 9000, 0],
    "CP6" : [12000, 9000, 0],
    "CP7" : [9000, 9000, 0],
    "CP8" : [6000, 9000, 0],
    "CP9" : [0, 9000, 0],
    # ネット原点側（下、上、アンテナ先）、逆側（下、上、アンテナ先）
    "CP10": [9000, 0, netHeight - 1000],
    "CP11": [9000, 0, netHeight],
    "CP12": [9000, 0, netHeight + 800],
    "CP13": [9000, 9000, netHeight - 1000],
    "CP14": [9000, 9000, netHeight],
    "CP15": [9000, 9000, netHeight + 800]
}

objectPoints = [
    objectDict["CP0"],
    objectDict["CP1"],
    objectDict["CP2"],
    objectDict["CP3"],
    objectDict["CP4"],  
    objectDict["CP5"],
    objectDict["CP6"],
    objectDict["CP7"],
    objectDict["CP8"],
    objectDict["CP11"],
    objectDict["CP12"],
    objectDict["CP14"],
    objectDict["CP15"]
]

def getCoordCSV(fileName):
    table = []
    file = open(fileName, "r")
    reader = csv.reader(file)
    for row in reader:
        table.append(list(map(float, row)))
    file.close()
    return table

if __name__ == "__main__":
    print(getCoordCSV(OUTPUT_FILE))