import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json
import glob

jsonList = glob.glob("input_data/*.json")
count = 0

fig = plt.figure(figsize=(19.2,10.8))
ax  = plt.axes()

court1 = patches.Rectangle(xy=(0, 0), width = 6000, height=9000, facecolor="white", edgecolor="black", fill=True)
court2 = patches.Rectangle(xy=(6000, 0), width = 3000, height=9000, facecolor="white", edgecolor="black", fill=True)
court3 = patches.Rectangle(xy=(9000, 0), width = 3000, height=9000, facecolor="white", edgecolor="black", fill=True)
court4 = patches.Rectangle(xy=(12000, 0), width = 6000, height=9000, facecolor="white", edgecolor="black", fill=True)

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
      ax.text(data[person][0], data[person][1], person, size=20, horizontalalignment="center", verticalalignment="center")
      print(person, data[person][0], data[person][1])
  plt.savefig('output/sample{:0=3}.png'.format(count))
  count += 1
  ax.clear()