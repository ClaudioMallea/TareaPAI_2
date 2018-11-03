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


def Normalizar(Vector):
    suma=0
    for dato in Vector:
        suma=suma+dato*dato
    VectorNormalizado = [x / (sqrt(suma)) for x in Vector]

    return VectorNormalizado


#C:\Users\Claudito\PycharmProjects\ProcesamientoImagenes\Python\images\gray\four_coins.png
#C:\Users\Claudito\PycharmProjects\ProcesamientoImagenes\Python\images\color\flower.jpg
#filename = 'C:\Users\Claudito\PycharmProjects\TareaPai2\chr_0\img001-00001.png'


file_list = os.listdir(".\chr_0")
data=[]
mask_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
mask_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

for p in file_list:
    print(p)
    image = io.imread('.\chr_0\\' + p)




    #Sobel gy:

    gy=ndimage.convolve(image,mask_y, mode='constant', cval=0.0)


    #Sobel gx:
    gx=ndimage.convolve(image,mask_x, mode='constant', cval=0.0)

    G=np.zeros((len(gy),len(gy[0])),dtype='int64')



    G= hypot(gy,gx)



    Phi=np.zeros((len(gy),len(gy[0])))
    for j in range(len(gy[0])):
        for i in range(len(gy)):
            Phi[i][j]= atan2(gy[i][j],gx[i][j])




    #histograma de orientaciones conteo ponderado:
    K=16
    angulo=0
    FV2=np.zeros(16)
    idx= (((angulo/pi)*K)%K)
    for j in range(len(gy[0])):
        for i in range(len(gy)):
            angulo=Phi[i][j]


            idx = int(round((angulo / pi) * K) % K)

            FV2[idx]=FV2[idx]+G[i][j]


    FV2=Normalizar(FV2)
    print("FV2")
    data.append(FV2)

np.savez('hola2.npz', *data)



