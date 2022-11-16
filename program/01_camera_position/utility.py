import csv
OUTPUT_FILE = "./data/output.csv"

objectPoints = [
    [0, 0, 0],
    #[900, 0, 0],
    [1800, 0, 0],
    [1800, 900, 0],
    #[900, 900, 0],
    [0, 900, 0],
    [900, 450, 0],
    [900, 450, 140]
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