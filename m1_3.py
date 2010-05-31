from os import listdir
from random import choice
import numpy as np
import pylab as mpl

from common import import_pics, show_image, IMAGE_PATH

# 1.3

# normalize the image
def normalize(im):
    # substract the mean
    im = im - im.mean()
    # divide by std
    im = im / im.std()
    return im

# normalize a set of images
def normalize_set(patches):
  array = np.zeros((len(patches),len(patches[0])**2))
  for i in range(len(patches)):
    array[i] = np.reshape(patches[i],len(patches[i])**2)
  # compute mean and std for every pixel across all patches
  mean = np.mean(array, axis=0)
  std = np.std(array, axis=0)
  for i in range(len(array)):
    # substract set mean from every patch and divide by std
    array[i] = (array[i] - mean)/std
  for i in range(len(patches)):
    patches[i] = np.reshape(array[i],(len(patches[i]),len(patches[i])))  
  return patches

# get random patch of size 'size * size' from an image
def get_patch(im, size):
  x = np.random.randint(0, im.shape[1] - size)
  y = np.random.randint(0, im.shape[0] - size)
  return im[y:y+size, x:x+size]

# get n random patches 'size * size' from an image
def get_patches(n, im, size):
  patches = []
  for i in range(n):
    patches.append(get_patch(im, size))
  return patches
  
def main():
  # tryout
  image_list = listdir(IMAGE_PATH)
  im = import_pics(choice(image_list))
  patch = get_patch(im,16)
  patch = normalize(patch)
  patches = get_patches(10, im, 16)
  patches = normalize_set(patches)

if __name__ == '__main__':
  main()




