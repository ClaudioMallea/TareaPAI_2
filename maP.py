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




def maximo(vector):
    max=-10000
    posicion=0
    for x in range(len(vector)):
        if (max<vector[x]):
            max=vector[x]
            posicion=x
    return (max,posicion)





def distancia(Vector1, Vector2):
    suma=0
    for x in range(len(Vector1)):
        suma=suma+((Vector1[x]-Vector2[x])*(Vector1[x]-Vector2[x]))


    distancia=(sqrt(suma))
    return distancia

def Normalizar(Vector):
    suma=0
    for dato in Vector:
        suma=suma+dato*dato
    VectorNormalizado = [x / (sqrt(suma)) for x in Vector]

    return VectorNormalizado

Ks=input('Indique K: ')
metodo=input('Indique metodo: ')


MAP=0
44
MAPLISTA=[]
MAPLISTA.append(".\\test\chr_0\img001-00003.png")
MAPLISTA.append(".\\test\chr_0\img001-00059.png")
MAPLISTA.append(".\\test\chr_0\img001-00076.png")
MAPLISTA.append(".\\test\chr_0\img001-00081.png")
MAPLISTA.append(".\\test\chr_1\img002-00003.png")
MAPLISTA.append(".\\test\chr_1\img002-00058.png")
MAPLISTA.append(".\\test\chr_1\img002-00076.png")
MAPLISTA.append(".\\test\chr_1\img002-00081.png")
MAPLISTA.append(".\\test\chr_2\img003-00011.png")
MAPLISTA.append(".\\test\chr_2\img003-00113.png")
MAPLISTA.append(".\\test\chr_2\img003-00049.png")
MAPLISTA.append(".\\test\chr_2\img003-00102.png")
MAPLISTA.append(".\\test\chr_3\img004-00007.png")
MAPLISTA.append(".\\test\chr_3\img004-00008.png")
MAPLISTA.append(".\\test\chr_3\img004-00088.png")
MAPLISTA.append(".\\test\chr_3\img004-00095.png")
MAPLISTA.append(".\\test\chr_4\img005-00003.png")
MAPLISTA.append(".\\test\chr_4\img005-00069.png")
MAPLISTA.append(".\\test\chr_4\img005-00076.png")
MAPLISTA.append(".\\test\chr_4\img005-00089.png")
MAPLISTA.append(".\\test\chr_5\img006-00001.png")
MAPLISTA.append(".\\test\chr_5\img006-00058.png")
MAPLISTA.append(".\\test\chr_5\img006-00089.png")
MAPLISTA.append(".\\test\chr_5\img006-00040.png")
MAPLISTA.append(".\\test\chr_6\img007-00002.png")
MAPLISTA.append(".\\test\chr_6\img007-00076.png")
MAPLISTA.append(".\\test\chr_6\img007-00094.png")
MAPLISTA.append(".\\test\chr_6\img007-00043.png")
MAPLISTA.append(".\\test\chr_7\img008-00020.png")
MAPLISTA.append(".\\test\chr_7\img008-00007.png")
MAPLISTA.append(".\\test\chr_7\img008-00051.png")
MAPLISTA.append(".\\test\chr_7\img008-00074.png")
MAPLISTA.append(".\\test\chr_8\img009-00001.png")
MAPLISTA.append(".\\test\chr_8\img009-00058.png")
MAPLISTA.append(".\\test\chr_8\img009-00076.png")
MAPLISTA.append(".\\test\chr_8\img009-00091.png")
MAPLISTA.append(".\\test\chr_9\img010-00008.png")
MAPLISTA.append(".\\test\chr_9\img010-00018.png")
MAPLISTA.append(".\\test\chr_9\img010-00046.png")
MAPLISTA.append(".\\test\chr_9\img010-00085.png")
MAPLISTA.append(".\\test\chr_K\img021-00002.png")
MAPLISTA.append(".\\test\chr_K\img021-00026.png")
MAPLISTA.append(".\\test\chr_K\img021-00076.png")
MAPLISTA.append(".\\test\chr_K\img021-00091.png")


file_list = os.listdir(".\K"+Ks +metodo)


contador1=0
for nombreImagen in MAPLISTA:
    image = io.imread(nombreImagen)
    LetraDeLaImagen=nombreImagen[11]

    mask_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    mask_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    image = image * 1.0

    # Sobel gy:

    gy = ndimage.convolve(image, mask_y, mode='constant', cval=0.0)

    # Sobel gx:
    gx = ndimage.convolve(image, mask_x, mode='constant', cval=0.0)

    G = np.zeros((len(gy), len(gy[0])), dtype='int64')

    G = hypot(gy, gx)

    G=G*1.0

    Phi = np.zeros((len(gy), len(gy[0])))

    for j in range(len(gy[0])):
        for i in range(len(gy)):
            Phi[i][j] = atan2(gy[i][j], gx[i][j])

    # histograma de orientaciones conteo simple:
    K = int(Ks)



    if(metodo=="I"):
        angulo = 0

        FV = np.zeros(K)
        idx = (((angulo / pi) * K) % K)
        for j in range(len(gy[0])):
            for i in range(len(gy)):
                angulo = Phi[i][j]
                if (angulo < 0):
                    angulo = angulo + pi
                valor = ((angulo / pi) * K) % K
                cielo = int(ceil(valor))
                piso = int(floor(valor))

                a = valor - piso

                b = cielo - valor
                if (cielo == K):
                    FV[0] = FV[0] + (G[i][j] * b)
                    FV[piso] = FV[piso] + (G[i][j] * a)
                else:
                    FV[cielo] = FV[cielo] + (G[i][j] * b)
                    FV[piso] = FV[piso] + (G[i][j] * a)

        FV = Normalizar(FV)

    elif(metodo=="P"):
        angulo = 0

        FV = np.zeros(K)
        idx = (((angulo / pi) * K) % K)
        for j in range(len(gy[0])):
            for i in range(len(gy)):
                angulo = Phi[i][j]

                if (angulo < 0):
                    angulo = angulo + pi

                idx = int(round((angulo / pi) * K) % K)
                FV[idx] = FV[idx] + G[i][j]
        FV = Normalizar(FV)

    else:
        angulo = 0

        FV = np.zeros(K)
        idx = (((angulo / pi) * K) % K)
        for j in range(len(gy[0])):
            for i in range(len(gy)):
                angulo = Phi[i][j]

                if (angulo < 0):
                    angulo = angulo + pi

                idx = int(round((angulo / pi) * K) % K)
                FV[idx] = FV[idx] + 1
        FV = Normalizar(FV)





    ranking= np.ones(10)
    ranking=ranking*10.0








    min=10000
    listanombres=np.array([(1,'array','a'),(1,'array','a'),(1,'array','a'),(1,'array','a'),(1,'array','a'),(1,'array','a'),(1,'array','a'),(1,'array','a'),(1,'array','a'),(1,'array','a')])

    contador=0
    for i in file_list:


        for x in np.load(".\K"+Ks+metodo+"\\"+i):
            if(contador==180):
                contador=0
                break
            contador=contador+1


            FVOTRO=np.load(".\K"+Ks+"P\\"+i)[x]


            distancia1=distancia(FV,FVOTRO)
            valorMaximo=maximo(ranking)[0]
            posicionMaximo=maximo(ranking)[1]
            if(distancia1<maximo(ranking)[0]):
                ranking[posicionMaximo]=distancia1
                listanombres[posicionMaximo]=(distancia1,x,i)



    ranking.sort()
    listanueva=listanombres
    for y in range(len(ranking)):
        for x in listanombres:
            if (ranking[y]==x[0]):
                listanueva[y]=x
    i=0


    Listanueva=np.array(['a','a','a','a','a','a','a','a','a','a'])
    for x in listanueva:
        if(len(x[2])==9):
            Listanueva[i] = x[2][4]
            i=i+1
        else:

            Listanueva[i]=x[2][3]    #DEPENDE DEL METODO Y K
            i=i+1



    A=Listanueva==LetraDeLaImagen

    A=A.astype(int)


    B=A

    i=0

    for elemento in range(len(A)):
        if(A[elemento]==1):
            i=i+1
            B[elemento]=i
        else:
            B[elemento] = i




    C=range(1,len(B)+1)

    if(np.sum(A)==0.0):
        AP=0
    else:
        AP=np.sum(A*B/C)/np.sum(A)

    MAP=MAP+AP
    contador1=contador1+1
    print(str(contador1) +'/44')
map=MAP/44
print(map)