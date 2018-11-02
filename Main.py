import numpy as np
import skimage
import os
from skimage import data
from skimage import io
import matplotlib.pylab as plt
from skimage import color
from skimage.filters import threshold_adaptive

filename = input("Inserte la dirección de la imagen con el RUN a reconocer: " )


#filename = 'C:\Users\Claudito\PycharmProjects\TareaPai2\chr_0\img001-00001.png'


image = io.imread(filename)
print(type(image))
print(image.shape)







