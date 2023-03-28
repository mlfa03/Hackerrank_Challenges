# Day 5 - Correlation and Regression Lines 

from math import *

byx = 4/5 # 0.8
bxy = 9/20 # 0.45

r = sqrt(byx*bxy)
#b = r*sy/sx
sx = 3.0
sy = byx*sx/r

print(floor(10*sy**2)/10)
