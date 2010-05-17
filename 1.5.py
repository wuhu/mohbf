from os import listdir
import numpy as np
from random import choice
import pylab as mpl

from common import import_pics, show_image, IMAGE_PATH
from m1_3 import get_patch, normalize_set

image_list = listdir(IMAGE_PATH)
patches = []
xy = 41
n = 5000
patches = []
for i in range(n):
  im = import_pics(choice(image_list))
  patches.append(get_patch(im,xy))

patches = normalize_set(patches)

avpatch = np.zeros((xy, xy))
for i in range(len(patches)):
  reference = patches[i][(xy-1)/2, (xy-1)/2]
  avpatch = avpatch + patches[i] * reference
  print i
mpl.figure()
mpl.imshow(avpatch)
mpl.show()
