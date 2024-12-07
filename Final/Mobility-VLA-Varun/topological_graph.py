import networkx as nx
import re
import cv2
import matplotlib.pyplot as plt
import math


class Environment():
  def __init__(self, vid_filename, cam_locs_filename):
    vidcap = cv2.VideoCapture(vid_filename)
    success, image = vidcap.read()
    count = 0
    self.frames = {}
    self.cam_data = {}
    self.G = nx.Graph()
    self.epsilon = 0.1
    
    # print('self.cam_data', self.cam_data)

    while success:
      cv2.imwrite("assets/frames/frame%d.png" % count, image)     # save frame as JPEG file
      self.frames[count] = image
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
    
    # print('self.cam_data', self.cam_data)
    for i in range(count):
          self.cam_data[i] = {}

    for file_prefix in ['location0', 'location1', 'location2', 'rotation_euler0', 'rotation_euler1', 'rotation_euler2']:
      with open(cam_locs_filename + "/" + file_prefix + ".txt") as f:
        i = 0
        for line in f:
          # Use regex to extract x and y values
          match = re.search(r"{'x':([\d.]+), 'y':(-*[\d.]+)}", line)
          if match:
              x_value = float(match.group(1))
              y_value = float(match.group(2))
              self.cam_data[i][file_prefix] = y_value
          else:
            print("NO MATCH ERROR")
            print(file_prefix)
            print(i)
            print(line)
          i += 1
    for i in range(count):
      # print(self.cam_data[i])
      self.G.add_nodes_from([(i, self.cam_data[i] | {"frame": self.frames[i]})])

    # # Add edges based on node attributes
    for node1, attr1 in self.G.nodes(data=True):
        for node2, attr2 in self.G.nodes(data=True):
          if int(node1) == int(node2 - 1):
            self.G.add_edge(node1, node2, weight=self.node_distance(attr1, attr2))
          elif (not node1 == node2) and self.node_distance(attr1, attr2) < self.epsilon:
            self.G.add_edge(node1, node2, weight=self.node_distance(attr1, attr2))

    nx.draw(self.G)
    plt.show()

  def node_distance(self, attr1, attr2):
    return math.sqrt((attr1['location0'] - attr2['location0']) ** 2 + (attr1['location1'] - attr2['location1']) ** 2 + (attr1['location2'] - attr2['location2']) ** 2)

if __name__ == "__main__":
  env = Environment('assets/walkthrough.mp4', 'assets/cam_locs')
