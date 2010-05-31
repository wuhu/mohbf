from os import listdir
from random import choice
import numpy as np
import pylab as mpl

from common import import_pics, show_image, IMAGE_PATH
from 1.3 import get_patch, normalize_set

# take 500 random images and slice out 16x16 patches
image_list = listdir(IMAGE_PATH)
patches = []
for i in range(500)
  im = import_pics(choice(image_list))
  patches.append(get_patch(im,16))
  patches = normalize_set(patches)

# generate white noise images
noises = []
for i in range(500)
  noises.append(np.random.normal(0, 15000, (16, 16)))
  normalize_set(noises)
  noises = normalize_set(noises)

# generate smoothed white noise images
fnoises = []
for i in range(500)
  noise = np.random.normal(0, 15000, (16, 16))
  n = 9
  fnoises.append(convolve2d(noise, np.ones((n, n)) / (n * n), mode="same", boundary="symm"))
  fnoises = normalize_set(fnoises)

