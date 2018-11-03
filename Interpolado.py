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

    # histograma de orientaciones conteo ponderado interpolado:
    K=16
    angulo = 0
    FV3 = np.zeros(16)
    idx = (((angulo / pi) * K) % K)
    for j in range(len(gy[0])):
        for i in range(len(gy)):
            angulo = Phi[i][j]

            valor = ((angulo / pi) * K) % K
            cielo = int(ceil(valor))
            piso = int(floor(valor))
            a = valor - piso
            b = cielo - valor
            FV3[cielo] = FV3[cielo] + G[i][j] * b
            FV3[piso] = FV3[piso] + G[i][j] * a

    FV3 = Normalizar(FV3)
    print("FV3")
    data.append(FV3)

np.savez('hola3.npz', *data)



