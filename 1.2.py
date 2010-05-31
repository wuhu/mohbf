import numpy as np
import pylab as mpl
from scipy.signal import convolve2d

from common import import_pics, show_image

# 1.2
# import an image
im = import_pics("imk01765.tiff")

# a)
# add white noise using different variances
for i in (100, 1000, 5000, 10000, 30000):
    # generate white noise
    whiten = np.random.normal(0, i, (1020, 1532))
    # add the noise to the image
    imnoise = im + whiten
    # show image
    show_image(imnoise, "Noise added (sigma=%d)" % i)

# b)

# generate white noise
whiten = np.random.normal(0, 15000, (1020, 1532))
kernels = (3, 5, 9, 15, 29)
for n in kernels:
    # create smooth white noise by convolving white noise with a rectangular window
    tmp = convolve2d(whiten, np.ones((n, n)) / (n * n),
                     mode="same", boundary="symm")
    show_image(im + tmp, "Noise kernel (%d,%d)" % (n, n))

# first manual approach (with 1-d vector)
# for i in range(1532*1020):
#      tmp = 0
#     for j in range(-n/2,n/2):
#         for k in np.arange(-1532*(n/2), 1532*(n/2), 1532):
#             c = np.max(np.min(i+j+k, 1532*1020 - 1), 0)
#             tmp += whiten[c]
#     imav[i] += tmp / 9.
#     # show progress
#     if i % 1000 == 0:
#         print i
#     if i == 100000:
#         break

mpl.show()
