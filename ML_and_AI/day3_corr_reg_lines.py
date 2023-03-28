# Day 3 - Correlation and Regression Lines 

import math 
import statistics as st 

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]          
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]  

#Y = Bx + a
#We need to define de equation to calculate Y for X = 10
# a = intercept 
# b = slope

mean_x = st.mean(X)
mean_y = st.mean(Y)

sum_num_cov = 0
var_x = 0
for i in range(len(X)):
    sum_num_cov += (X[i] - mean_x)*(Y[i] - mean_y)
    var_x += (X[i] - mean_x)**2

# B = sample covariance / sample variance
B = sum_num_cov / var_x

#a = Y - Bx 
# x= 10
a = mean_y - B*mean_x

#Y = Bx + 
result_y = B*10 + a
print(round(result_y, 1))
