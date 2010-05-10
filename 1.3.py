from os import listdir
from random import choice
import numpy as np
import pylab as mpl

from common import import_pics, show_image, IMAGE_PATH

# 1.3

def normalize(im):
    im = im - im.mean()
    im = im / im.std()
    return im

n = 16 # patch size
image_list = listdir(IMAGE_PATH)
im = import_pics(choice(image_list))
x = np.random.randint(0, im.shape[1] - n)
y = np.random.randint(0, im.shape[0] - n)
patch = im[y:y+n, x:x+n]
patch = normalize(patch)

mpl.imshow(patch)
mpl.show()
