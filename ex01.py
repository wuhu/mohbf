from PIL import Image
import numpy as np
import pylab as mpl

def show_image(im):
    image = Image.new("P",(1532,1020))
    image.putdata([float(i)/16**2 for i in im])
    mpl.figure()
    mpl.imshow(image)

# 1.1

mpl.rcParams['image.interpolation'] = 'nearest'

def import_pics(filename):
    im = Image.open("/home/mohbf/images/"+filename)
    return np.array(im.getdata())

im = import_pics("imk01765.tiff")
show_image(im)

# 1.2    

# a)

#for i in (100, 1000, 5000, 10000, 30000):
#    imnoise = [j + np.random.normal(0, i) for j in im]
#    show_image(imnoise)

# b)

whiten = [np.random.normal(0, 15000) for i in range(1532*1020)]

imav = np.array(im)

n = 29

for i in range(1532*1020):
    tmp = 0
    for j in range(-n/2,n/2):
        for k in np.arange(-1532*(n/2), 1532*(n/2), 1532):
            c = np.max(np.min(i+j+k, 1532*1020 - 1), 0)
            tmp += whiten[c]
    imav[i] += tmp / 9
    # show progress
    if i % 1000 == 0:
        print i
    if i == 100000:
        break

show_image(imav)

mpl.show()

