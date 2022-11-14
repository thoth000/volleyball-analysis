import csv
OUTPUT_FILE = "./data/output.csv"

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