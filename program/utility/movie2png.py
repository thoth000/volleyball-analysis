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
  count = 0
  split = 5

  while True:
    if n % split == 0:
      ret, frame = cap.read()
      if ret:
        print("image_{}.png".format(count))
        cv2.imwrite('{}_{}.{}'.format(base_path, str(count).zfill(digit), ext), frame)
        count+=1
      else:
        return
    n+=1

save_all_frames('sample.mp4', 'output', 'image')