from PIL import Image
import numpy as np
import pylab as mpl

mpl.rcParams['image.interpolation'] = 'nearest'
mpl.gray()

IMAGE_PATH = "/home/mohbf/images/"
IMAGE_SHAPE = (1020, 1532)

# function shows an image using pylab
def show_image(image, title=None):
    mpl.figure()
    if title:
        mpl.title(title)
    mpl.imshow(image)

# import an image from IMAGE_PATH
def import_pics(filename):
    im = Image.open(IMAGE_PATH + filename).getdata()
    im = np.reshape(im, IMAGE_SHAPE)
    return np.array(im)
