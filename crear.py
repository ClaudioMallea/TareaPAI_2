import numpy as np
import skimage
import os
from skimage import data
from skimage import io
import matplotlib.pylab as plt
from scipy import ndimage
from skimage import color
from skimage.filters import threshold_adaptive
from math import *
from numpy import hypot




for x in np.load('.\\hola.npz'):
    print(x)