import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='png'):
  cap = cv2.VideoCapture(video_path)

  if not cap.isOpened():
    return

  os.makedirs(dir_path, exist_ok=True)
  base_path = os.path.join(dir_path, basename)

  digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

  n = 0
  split = 15

  while True:
    ret, frame = cap.read()
    if n % split == 0:
      if ret:
        print("image_{}.png".format(n//15))
        cv2.imwrite('{}_{}.{}'.format(base_path, str(n//15).zfill(digit), ext), frame)
      else:
        return
    n+=1

save_all_frames('IMG_1146.MOV', 'output', 'image')