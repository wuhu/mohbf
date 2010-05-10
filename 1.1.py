import pylab as mpl

from common import import_pics, show_image

im = import_pics("imk01765.tiff")
show_image(im, "Original")

mpl.show()
