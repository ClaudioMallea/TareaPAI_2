import numpy as np
import skimage
import os
from skimage import data
from skimage import io
import matplotlib.pylab as plt
from scipy import ndimage
from skimage import color
from skimage.filters import threshold_adaptive
from math import sqrt
from math import atan2
from math import pi
filename = input("Inserte la dirección de la imagen con el RUN a reconocer: " )
#C:\Users\Claudito\PycharmProjects\ProcesamientoImagenes\Python\images\gray\four_coins.png
#C:\Users\Claudito\PycharmProjects\ProcesamientoImagenes\Python\images\color\flower.jpg
#filename = 'C:\Users\Claudito\PycharmProjects\TareaPai2\chr_0\img001-00001.png'


image = io.imread(filename)

io.imsave("Imagen_Con_BoundingBox.jpg",image, plugin=None)
imgplot = plt.imshow(image,cmap='gray')
plt.show()


print(type(image))
print(image.shape)

mask_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
mask_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

print(type(mask_y))
print(mask_y)






#Sobel gy:

gy=ndimage.convolve(image,mask_y, mode='constant', cval=0.0)


io.imsave("gy.jpg",gy, plugin=None)

#Sobel gx:
gx=ndimage.convolve(image,mask_x, mode='constant', cval=0.0)
io.imsave("gx.jpg",gx, plugin=None)

G=np.zeros((len(gy),len(gy[0])),dtype=int)


for j in range(len(gy[0])):
    for i in range(len(gy)):
        G[i][j]= sqrt((gx[i][j]*gx[i][j])+(gy[i][j]*gy[i][j]))

io.imsave("G.jpg",G, plugin=None)


Phi=np.zeros((len(gy),len(gy[0])))
for j in range(len(gy[0])):
    for i in range(len(gy)):
        Phi[i][j]= atan2(gy[i][j],gx[i][j])




#histograma de orientaciones:
K=16
angulo=0
FV=np.zeros(16,dtype=int)
idx= (((angulo/pi)*K)%K)
for j in range(len(gy[0])):
    for i in range(len(gy)):
        angulo=Phi[i][j]
        idx = int(round((angulo / 3.1415) * K) % K)

        FV[idx]=FV[idx]+1


print(FV[0])
print(FV[1])
print(FV[2])
print(FV[3])
print(FV[4])
print(FV[5])
print(FV[6])
print(FV[7])
print(FV[8])
print(FV[9])
print(FV[10])
print(FV[11])
print(FV[12])
print(FV[13])
print(FV[14])
print(FV[15])





