# Day 2 - Correlation and Regression Lines 

import statistics as st
import math 

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

mean_x = st.mean(X)
mean_y = st.mean(Y)

 
sum_num_cov = 0 
var_x = 0
var_y = 0

for i in range(len(X)):
    sum_num_cov += (X[i] - mean_x)*(Y[i] - mean_y)
    var_x += (X[i] - mean_x)**2
    var_y += (Y[i] - mean_y)**2

r = sum_num_cov / (math.sqrt(var_x*var_y))
std_x = st.stdev(X)      #math.sqrt(var_x/len(X))
std_y = st.stdev(Y)      #math.sqrt(var_y/len(Y))

slope = (r*std_y)/std_x
print(round(slope,3))
