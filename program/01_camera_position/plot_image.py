from matplotlib import pyplot as plt
from matplotlib import image as img
import cv2

from utility import *

# テキストファイルに座標を出力
def clickImage(event):
    if event.xdata != None:
        output_file = open(OUTPUT_FILE, "a")
        print("button={}, x={}, y={}".format(event.button, event.xdata, event.ydata))
        output_file.write("{},{}\n".format(event.xdata, event.ydata))
        output_file.close()

def getImagePoints(image, changeColor = False):
    # window : 画面ID
    window = plt.figure(figsize = (16, 9))
    # windowに画像を表示
    if changeColor:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(image)
    # クリック関数割り当て
    clickID = window.canvas.mpl_connect("button_press_event", clickImage)
    # 画面表示
    plt.show()

##########################################

if __name__ == "__main__":
    image = cv2.imread("../00_calibration/iPhone_image/resize/1.png")
    imagePoints = []
    getImagePoints(image, True)
    print(imagePoints)