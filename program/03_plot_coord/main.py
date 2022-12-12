import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.figure(figsize=(19.2,10.8))
ax  = plt.axes()

court1 = patches.Rectangle(xy=(0, 0), width = 600, height=900, facecolor="white", edgecolor="black", fill=True)
court2 = patches.Rectangle(xy=(600, 0), width = 300, height=900, facecolor="white", edgecolor="black", fill=True)
court3 = patches.Rectangle(xy=(900, 0), width = 300, height=900, facecolor="white", edgecolor="black", fill=True)
court4 = patches.Rectangle(xy=(1200, 0), width = 600, height=900, facecolor="white", edgecolor="black", fill=True)
ax.add_patch(court1)
ax.add_patch(court2)
ax.add_patch(court3)
ax.add_patch(court4)

plt.xlim(0, 1800)
plt.ylim(0, 900)

# plt.plot(900, 450, marker=".", color = "white")

ax.text(920, 450, "1", size=20, horizontalalignment="center", verticalalignment="center")

plt.savefig('sample.png')