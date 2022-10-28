import cv2
import numpy as np
import glob
filename = "./pattern.png"
 
# Chessboard dimensions
number_of_squares_X = 10 # Number of chessboard squares along the x-axis
number_of_squares_Y = 7  # Number of chessboard squares along the y-axis
nX = number_of_squares_X - 1 # Number of interior corners along x-axis
nY = number_of_squares_Y - 1 # Number of interior corners along y-axis
 
def main():
  # Load an images
  img_dir = "./iPhone_image"
  img_path = f"{img_dir}/resize/*.png"
  
  file_list = glob.glob(img_path)
  i = 1
  for filename in file_list:
    image = cv2.imread(filename)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    # Find the corners on the chessboard
    success, corners = cv2.findChessboardCorners(gray, (nY, nX), None)
    # If the corners are found by the algorithm, draw them
    if success == True:
    # Draw the corners
      cv2.drawChessboardCorners(image, (nY, nX), corners, success)
    # Create the output file name by removing the '.jpg' part
      new_filename = f"{img_dir}/draw/{i}.png"
    # Save the new image in the working directory
      cv2.imwrite(new_filename, image)
    i+=1
main()