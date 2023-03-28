import numpy as np 

#F - Number of observed features
#N - Number of rows for which features as well as price per sqft have been noted
F, N = list(map(int, input().split()))

#Initializing X and Y
X = []
Y = []
for i in range(N):
    #Populating the rows:
    x = input()
    x = x.strip().split(' ')
    x = [float(a) for a in x]
    X.append(x[0:F])  #features columns
    Y.append(x[F:])   #Last column: price per square foot

q = input()
q = int(q.strip())

X_test = []
for i in range(q):
    x_test = input()
    x_test = x_test.strip().split(' ')
    x_test = [float(a) for a in x_test]
    X_test.append(x_test)


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

poly = PolynomialFeatures(degree=3)
poly.fit(np.array(X))

regression = LinearRegression()
regression.fit(poly.transform(np.array(X)), Y)

Y_test = regression.predict(poly.transform(np.array(X_test)))
for y_test in Y_test:
    print(round(y_test[0], 2))
