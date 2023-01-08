import cv2
import os
import numpy as np
import glob
import sys

# 動画から画像への変換
def save_all_frames(video_path, dir_path, ext='png'):
  cap = cv2.VideoCapture(video_path)

  if not cap.isOpened():
    return

  digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

  n = 0

  while True:
    ret, frame = cap.read()
    if ret:
      outPath = dir_path + "/{}.{}".format(str(n).zfill(digit), ext)
      cv2.imwrite(outPath, frame)
      print("created", outPath)
    else:
      return
    n+=1


c_dir      = "../../data/calibration"
movie_path = "../../data/origin_movie/01_camera2.mp4"
splited_images_dir = "splited_images"
undistorted_images_dir = "undistorted_images"

cMat     = np.loadtxt("{}/camera_mat.csv".format(c_dir), delimiter=",")
dist     = np.loadtxt("{}/dist.csv".format(c_dir), delimiter=",")

# 出力ディレクトリの生成
os.makedirs(splited_images_dir, exist_ok=True)
os.makedirs(undistorted_images_dir, exist_ok=True)

# フレームごとに分解
save_all_frames(movie_path, splited_images_dir)

# フレームごとに歪み除去
imageFiles = glob.glob(splited_images_dir + "/*.png")
digit = len(str(len(imageFiles)))

for index, imageFile in enumerate(imageFiles):
  img = cv2.imread(imageFile)
  
  dst = cv2.undistort(img, cMat, dist)
  
  outPath = undistorted_images_dir + "/{}.png".format(str(index).zfill(digit))
  cv2.imwrite(outPath, dst)
  print("created", outPath)


# 画像から動画への変換

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

if movie_path == "../../data/origin_movie/01_camera2.mp4":
  fourcc = cv2.VideoWriter_fourcc(*'HEVC')

video = cv2.VideoWriter('output.mp4',fourcc, 30.0, (1920, 1080))

images = glob.glob(undistorted_images_dir + "/*.png")

if not video.isOpened():
    print("can't be opened")
    sys.exit()

for imgFile in images:
    img = cv2.imread(imgFile)

    # can't read image, escape
    if img is None:
        print("can't read")
        break

    # add
    video.write(img)

video.release()
print("created movie")