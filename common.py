from PIL import Image
import numpy as np
import pylab as mpl

mpl.rcParams['image.interpolation'] = 'nearest'
mpl.gray()

IMAGE_PATH = "/home/mohbf/images/"
IMAGE_SHAPE = (1020, 1532)

def show_image(image, title=None):
    mpl.figure()
    if title:
        mpl.title(title)
    mpl.imshow(image)

def import_pics(filename):
    im = Image.open(IMAGE_PATH + filename).getdata()
    im = np.reshape(im, IMAGE_SHAPE)
    return np.array(im)
