# Temperature Predictions 
# Enter your code here. Read input from STDIN. Print output to STDOUT
# SOLUTION 1: 100% 
import numpy as np
import pandas as pd

n = int(input())

columns = input().split("\t")

years = []
months = []
ttmax = []
ttmin = []

missing = []
for i in range(n):
    l = input().split("\t")

    years.append(int(l[0]))
    months.append(l[1])
    
    #print(l[2])
    if 'Missing' in l[2]:
        ttmax.append(np.nan)
        missing.append([i, "min"])
    else:
        ttmax.append(float(l[2]))
        
    if 'Missing' in l[3]:
        ttmin.append(np.nan)
        missing.append([i, "max"])
    else:
        ttmin.append(float(l[3]))
        
dic = {}
for col, value in zip(columns, [years, months, ttmin, ttmax]):
    dic[col] = value

df = pd.DataFrame(dic)
df=df.interpolate(method="quadratic")
for miss in missing:
    if miss[1] == "min":
        print(round(df.iloc[miss[0]]['tmin'], 1))
    else:
        print(round(df.iloc[miss[0]]['tmax'], 1))

#SOLUTION 2: 61% 
import numpy as np 
from sklearn.ensemble import GradientBoostingRegressor

#Data range from 01/1908 to 03/2012
#some lines are replaced by 'Missing'
#ESTIMATE MISSING VALUES 

#Dict for the Months
month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

#Function to check presence of numbers in temperatures:
def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

#N is number of rows in the first line
N = int(input())
#Lines with the information: 0-year | 1-month | 2-max_temp | 3-min_temp , tab-separated
input()

MIN = []
MAX = []
X_train = []
X_test = []

for i in range(N):
    myrow = input().split('\t')
    MAX.append(float(myrow[2]) if is_float(myrow[2]) else None) #column with max temp
    MIN.append(float(myrow[3]) if is_float(myrow[3]) else None) #column with min temp
    if is_float(myrow[2]) and is_float(myrow[3]):  #if both are present, append to Xtrain
        X_train.append([int(myrow[0]), month[myrow[1]]])
    else:
        X_test.append([int(myrow[0]), month[myrow[1]]]) #If it's Missing, add these rows to testing because these values will be predicted, since they are missing 

#Ytrain is the average values of max and min temperatures:
Y_train = ([(x + y)/2 for x, y in zip(MAX, MIN) if x is not None and y is not None])

model = GradientBoostingRegressor()
model.fit(X_train, Y_train)

Y_test = list(model.predict(X_test))
#Estimate and print missing values
#Pop removes the item at the given index from the list and returns the removed item.
for i in range(N):
    if MIN[i] == None:
        print(round(2 * Y_test.pop(0) - MAX[i], 1)) #Interpolate to print min value missing
    if MAX[i] == None:
        print(round(2 * Y_test.pop(0) - MIN[i], 1)) #Interpolate to print max value missing
