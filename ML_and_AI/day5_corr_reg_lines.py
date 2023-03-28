# Day 5 - Correlation and Regression Lines

import statistics as st 
import math 

#input: N M P C - number of student, math, physics, chemistry

    
def linear_correlation(X, Y):
    n = len(X)
    numerator = (n * sum(X[i] * Y[i] for i in range(n)) - sum(X) * sum(Y))
    denominator = math.sqrt((n * sum(v ** 2 for v in X) - sum(X) ** 2) * (n * sum(v ** 2 for v in Y) - sum(Y) ** 2))
    p_coefficient = numerator / denominator

    return p_coefficient

#The strip() method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).
#First row contains integer N - number of students
#Following N rows contains M P C separated by tab space ('\t')

N = int(input().strip())   #to get the size of the data

M = []
P = []
C = []
for i in range(N):
    x = input()
    x = x.strip().split('\t')
    x = [float(a) for a in x]
    M.append(x[0])
    P.append(x[1])
    C.append(x[2])

print(round(linear_correlation(M, P), 2))
print(round(linear_correlation(P, C), 2))
print(round(linear_correlation(C, M), 2))
