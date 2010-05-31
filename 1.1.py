import pylab as mpl

from common import import_pics, show_image

# (see common.py for the implementation of the functions used below)
# import an image from the database
im = import_pics("imk01765.tiff")
# show it
show_image(im, "Original")

mpl.show()
