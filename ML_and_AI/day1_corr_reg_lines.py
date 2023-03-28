# Day 1 - Correlation and Regression Lines 

import math 
import statistics as st

#def mean(data):
#    return sum(data) / len(data)

def var(data):    #defining without denominator because it cancels out in r formula
    sum = 0
    for i in range(len(data)):
        sum = sum + (data[i] - st.mean(data)) ** 2
    return sum

def cov(dt1, dt2):
    sum = 0
    for i in range(len(dt1)):
        sum += (dt1[i] - st.mean(dt1)) * (dt2[i] - st.mean(dt2))
    return sum
#dt1 - data point in physics 
#dt2 - data point in history

# Set data- add this list too to the 'test against custom input' box
physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

mean_physics = st.mean(physics)
mean_history = st.mean(history)

var_physics = var(physics)
var_history = var(history)

cov = cov(physics, history)
std = math.sqrt(var_physics * var_history)

# Correlation
r = cov / std
print(round(r, 3))
