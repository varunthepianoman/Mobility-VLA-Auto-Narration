import networkx

import cv2




class Environment():
  def __init__(self, filename):
    vidcap = cv2.VideoCapture(filename)
    success, image = vidcap.read()
    count = 0
    frames = {}
    cam_data = {}

    while success:
      cv2.imwrite("assets/frames/frame%d.png" % count, image)     # save frame as JPEG file
      frames[count] = image
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1

    for i in range(count):
      


if __name__ == "__main__":
  env = Environment('assets/walkthrough.mp4')
