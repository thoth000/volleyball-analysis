import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import json
import glob

jsonList = glob.glob("input_data/*.json")
count = 0

digit = len(str(len(jsonList)))

fig = plt.figure(figsize=(19.2,10.8))
ax  = plt.axes()

court1 = patches.Rectangle(xy=(0, 0), width = 6000, height=9000, facecolor="white", edgecolor="black", fill=True, linewidth = 10)
court2 = patches.Rectangle(xy=(6000, 0), width = 3000, height=9000, facecolor="white", edgecolor="black", fill=True, linewidth = 10)
court3 = patches.Rectangle(xy=(9000, 0), width = 3000, height=9000, facecolor="white", edgecolor="black", fill=True, linewidth = 10)
court4 = patches.Rectangle(xy=(12000, 0), width = 6000, height=9000, facecolor="white", edgecolor="black", fill=True, linewidth = 10)

outDir = "output"
os.makedirs(outDir, exist_ok=True)

textsize = 45

for file in jsonList:
  plt.xlim(0, 18000)
  plt.ylim(0, 9000)

  ax.add_patch(court1)
  ax.add_patch(court2)
  ax.add_patch(court3)
  ax.add_patch(court4)
  
  with open(file) as f:
    data = json.load(f)
    for person in data:
      # 座標軸変更の影響でxを9000で反転
      x = 9000*2 - data[person][0]
      if data[person][0] > 9000:
        ax.text(x, data[person][1], person, size=textsize, horizontalalignment="center", verticalalignment="center", color="red", fontweight="bold")
      else:
        ax.text(x, data[person][1], person, size=textsize, horizontalalignment="center", verticalalignment="center", color="blue", fontweight="bold")
  
  print(file)
  
  figFileName = "output/sanple{}.png".format(str(count).zfill(digit))
  plt.savefig(figFileName)
  count += 1
  ax.clear()