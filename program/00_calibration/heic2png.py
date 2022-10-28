import os
import glob

img_dir = "./iPhone_image"
img_path = f"{img_dir}/*.heic"

fileList = glob.glob(img_path)

i = 1

for file in fileList:
    os.rename(file, f"{img_dir}/{i}.png")
    i+=1