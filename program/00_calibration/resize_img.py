import os
import glob
import cv2

img_dir = "./iPhone_image"
img_path = f"{img_dir}/*.png"

file_list = glob.glob(img_path)
file_num = len(file_list)

i = 1

for i in range(1, file_num+1):
    file = "{}/{}.png".format(img_dir, i)
    img = cv2.imread(file)
    new_file = "{}/resize/{}.png".format(img_dir, i)
    img_resize = cv2.resize(img, (1920, 1080))
    cv2.imwrite(new_file, img_resize)