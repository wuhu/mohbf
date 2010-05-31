from os import listdir
import numpy as np
from random import choice
import pylab as mpl

from common import import_pics, show_image, IMAGE_PATH
from m1_3 import get_patch, normalize_set

# this currently takes extremely long and needs vast amounts of RAM!

# load images
image_list = listdir(IMAGE_PATH)
patches = []
xy = 41
n = 5000
patches = []
for i in range(n):
  im = import_pics(choice(image_list))
  patches.append(get_patch(im,xy))

patches = normalize_set(patches)

# Extract random patches from random images and calculate the
# correlations with respect to a reference pixel position.
avpatch = np.zeros((xy, xy))
for i in range(len(patches)):
  reference = patches[i][(xy-1)/2, (xy-1)/2]
  avpatch = avpatch + patches[i] * reference
  print i
mpl.figure()
mpl.imshow(avpatch)
mpl.show()

# the 1-D visualization is not implemented yet!

