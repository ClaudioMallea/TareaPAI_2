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
LISTA=[]
LISTA.append('K320.npz')
LISTA.append('K321.npz')
LISTA.append('K322.npz')
LISTA.append('K323.npz')
LISTA.append('K324.npz')
LISTA.append('K325.npz')
LISTA.append('K326.npz')
LISTA.append('K327.npz')
LISTA.append('K328.npz')
LISTA.append('K329.npz')
LISTA.append('K32K.npz')

LISTA2=[]
LISTA2.append(".\chr_0")
LISTA2.append(".\chr_1")
LISTA2.append(".\chr_2")
LISTA2.append(".\chr_3")
LISTA2.append(".\chr_4")
LISTA2.append(".\chr_5")
LISTA2.append(".\chr_6")
LISTA2.append(".\chr_7")
LISTA2.append(".\chr_8")
LISTA2.append(".\chr_9")
LISTA2.append(".\chr_K")
asdf = 0
for Z in LISTA2:

    file_list = os.listdir(Z)
    data=[]
    mask_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    mask_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    for p in file_list:
        print(p)
        image = io.imread(Z+'\\' + p)


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

        #histograma de orientaciones conteo simple:
        K=32
        angulo=0
        FV=np.zeros(32)
        idx= (((angulo/pi)*K)%K)
        for j in range(len(gy[0])):
            for i in range(len(gy)):
                angulo=Phi[i][j]
                idx = int(round((angulo / pi) * K) % K)
                FV[idx]=FV[idx]+1
        FV=Normalizar(FV)
        data.append(FV)
    np.savez(LISTA[asdf], *data)
    asdf=asdf+1


