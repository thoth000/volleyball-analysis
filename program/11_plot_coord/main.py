import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import json
import glob

jsonList = glob.glob("input/*.json")
count = 0

digit = len(str(len(jsonList)))

fig = plt.figure(figsize=(19.2,10.8))
ax  = plt.axes()

court1 = patches.Rectangle(xy=(0, 0), width = 6000, height=9000, facecolor="white", edgecolor="black", fill=True)
court2 = patches.Rectangle(xy=(6000, 0), width = 3000, height=9000, facecolor="white", edgecolor="black", fill=True)
court3 = patches.Rectangle(xy=(9000, 0), width = 3000, height=9000, facecolor="white", edgecolor="black", fill=True)
court4 = patches.Rectangle(xy=(12000, 0), width = 6000, height=9000, facecolor="white", edgecolor="black", fill=True)

outDir = "output"
os.makedirs(outDir, exist_ok=True)

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
      
      id = data[person]["c1_id"]
      ax.text(data[person]["position_x"], data[person]["position_y"], id, size=25, horizontalalignment="center", verticalalignment="center")
  
  print(file)
  
  figFileName = "output/{}.png".format(str(count).zfill(digit))
  # plt.savefig('output/sample{:0=3}.png'.format(count))
  plt.savefig(figFileName)
  count += 1
  ax.clear()