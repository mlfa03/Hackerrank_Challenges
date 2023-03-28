# Laptop Battery Life

import math
import os
import random
import re
import sys
import numpy as np
from sklearn import linear_model as lm
import pandas as pd


dataset = pd.read_csv('trainingdata.txt', header=None)

#First column: time the laptop was charged for
#Let's keep it a maximum of 3 hours , discarding other values in the dataset that seem unreal
dataset = dataset.loc[dataset[0] <= 3]

# Defining X and y 
X = np.array(dataset[0]).reshape(-1,1)   #time to charge battery
y = np.array(dataset[1]).reshape(-1,1)   #time battery lasted

model = lm.LinearRegression()
model.fit(X = X, y = y)


if __name__ == '__main__':
    timeCharged = float(input().strip())

predict = model.predict(np.array(timeCharged).reshape(-1,1))
predict = float(predict[0].round(2)) # for getting the standard output format

if predict > 8:
    print(8.0)
else:
    print(predict)
