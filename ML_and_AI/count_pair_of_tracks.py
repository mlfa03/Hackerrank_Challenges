# Count the pair of tracks 

import numpy as np
import math
import cmath
from io import StringIO
import scipy.ndimage as I
import scipy.misc as sm
import scipy.signal as ss

def myread():
    line1 = input().split()
    row, col = int(line1[0]),int(line1[1])
    img = np.zeros((row,col),dtype=float)
    flag = 0
    for j in range(row):
        line1 = input().split()
        for i in range(len(line1)):             
            b,g,r = line1[i].split(',')
            img[flag,i] = 0.2989*int(r) + 0.5870*int(g) + 0.1140*int(b)
        flag += 1
        
    return img,row,col


def garbor(img):
    g = np.zeros((3,3),dtype=complex)
    for x in range(-1,2):        
        for y in range(-1,2):
            g[x+1,y+1] = cmath.exp(-math.pi*(x**2+y**2))*(cmath.exp(-1j*2*math.pi*0.01*x)-cmath.exp(-math.pi*(0.01/1.5)**2))
   
    sigma = ss.fftconvolve(img,g,mode='same')
    return sigma   

img,row,col = myread()
sigma = garbor(img)

sig = np.imag(sigma)
sigmax = sig.max()
sigmin = sig.min()
for i in range(row):
    for j in range(col):
        sig[i,j] = (sig[i,j] - sigmin)/(sigmax-sigmin)*255.0
        if sig[i,j] < 170: sig[i,j] = 0
        else: sig[i,j] = 1
I.binary_opening(sig, structure=np.ones((10,10))).astype(np.int)
num = 11
for i in range(-15,15):
    a = sig[int(row*3/4) + i,10:col-10]
    b = a[1:] - a[:-1]
    tm = len(list(filter(lambda x: abs(x) == 1, b)))
    if tm < num:
        num = tm
        
num /= 2
if num==0:
    print(2)
elif num > 10:
    print(1)
elif num%2==0:
    print(int(num/2))
else:
    print(int(num/2))
