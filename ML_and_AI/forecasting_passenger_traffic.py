# Forecasting Passenger Traffic 

import numpy as np

N = int(input())
data = []
temp = []
for i in range(N):
     data.append(input().split())
     temp.append(float(data[i][1]))
     
     
from scipy import interpolate
leng = list(range(len((temp))))
interpolation = interpolate.interp1d(leng,temp,fill_value='extrapolate')

#Forecasting passenger traffic for the next 12 months
#If we have input data with 60 months, interpolation will be for range(60, 60+12)
y = interpolation(range(len(temp),len(temp)+12))
        
for x in y:
    print(x)
