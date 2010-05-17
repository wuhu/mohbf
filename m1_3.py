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

def normalize_set(patches):
  array = np.zeros((len(patches),len(patches[0])**2))
  for i in range(len(patches)):
    array[i] = np.reshape(patches[i],len(patches[i])**2)
  mean = np.mean(array, axis=0)
  std = np.std(array, axis=0)
  for i in range(len(array)):
    array[i] = (array[i] - mean)/std
  for i in range(len(patches)):
    patches[i] = np.reshape(array[i],(len(patches[i]),len(patches[i])))  
  return patches

def get_patch(im, size):
  x = np.random.randint(0, im.shape[1] - size)
  y = np.random.randint(0, im.shape[0] - size)
  return im[y:y+size, x:x+size]

def get_patches(n, im, size):
  patches = []
  for i in range(n):
    patches.append(get_patch(im, size))
  return patches
  
def main():
  image_list = listdir(IMAGE_PATH)
  im = import_pics(choice(image_list))
  patch = get_patch(im,16)
  patch = normalize(patch)

  patches = get_patches(10, im, 16)

  patches = normalize_set(patches)

if __name__ == '__main__':
  main()

#mpl.imshow(patches[0])
#mpl.figure()
#mpl.imshow(patches[0])
#mpl.imshow(np.std(np.array(patches),axis=0))
#mpl.imshow(patch)
#mpl.imshow(avg)
#mpl.show()




