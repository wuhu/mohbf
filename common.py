from PIL import Image
import numpy as np
import pylab as mpl

mpl.rcParams['image.interpolation'] = 'nearest'
mpl.gray()

def show_image(image, title=None):
    mpl.figure()
    if title:
        mpl.title(title)
    mpl.imshow(image)

def import_pics(filename):
    im = Image.open("/home/mohbf/images/"+filename).getdata()
    im = np.reshape(im, (1020, 1532))
    return np.array(im)
