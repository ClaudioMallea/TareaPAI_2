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

K=128
k=str(K)
LISTA=[]
LISTA.append('K'+k+'0.npz')
LISTA.append('K'+k+'1.npz')
LISTA.append('K'+k+'2.npz')
LISTA.append('K'+k+'3.npz')
LISTA.append('K'+k+'4.npz')
LISTA.append('K'+k+'5.npz')
LISTA.append('K'+k+'6.npz')
LISTA.append('K'+k+'7.npz')
LISTA.append('K'+k+'8.npz')
LISTA.append('K'+k+'9.npz')
LISTA.append('K'+k+'K.npz')

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

        image = io.imread(Z+'\\' + p)
        image=image*1.0

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

        angulo=0
        FV=np.zeros(K)
        idx= (((angulo/pi)*K)%K)
        for j in range(len(gy[0])):
            for i in range(len(gy)):
                angulo=Phi[i][j]

                if(angulo<0):
                    angulo=angulo+pi

                idx = int(round((angulo / pi) * K) % K)
                FV[idx]=FV[idx]+1
        FV=Normalizar(FV)
        data.append(FV)
    np.savez(LISTA[asdf], *data)
    asdf=asdf+1


