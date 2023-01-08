import sys
import cv2
import glob

# encoder(for mp4)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# output file name, encoder, fps, size(fit to image size)
video = cv2.VideoWriter('output.mp4',fourcc, 30.0, (1920, 1080))

images = glob.glob("input/*.png")

if not video.isOpened():
    print("can't be opened")
    sys.exit()

for imgFile in images:
    print(imgFile)
    img = cv2.imread(imgFile)

    # can't read image, escape
    if img is None:
        print("can't read")
        break

    # add
    video.write(img)

video.release()
print("created")