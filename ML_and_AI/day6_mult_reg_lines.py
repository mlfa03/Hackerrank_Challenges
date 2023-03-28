# Day 6: Multiple regression lines

#Get the prices for the houses that charlie could not get information on
# the price but has the features: 
#Input is 2-space separated integers - F and N
FN = input()
FN = FN.strip().split(' ')

F = int(FN[0])   #Number of observed features
N = int(FN[1])   #Number of rows/houses that have both features and preice

X = [] 
Y = []
#Getting X and Y for the samples that have features and price
for i in range(N):
    x = input()
    x = x.strip().split(' ')
    x = [float(a) for a in x]
    X.append(x[0:F])
    Y.append(x[F:])
#T - number of houses that have features but not price
T = input()
T = int(T.strip())

X_test = []
for i in range(T):
    x_test = input()
    x_test = x_test.strip().split(' ')
    x_test = [float(a) for a in x_test]
    X_test.append(x_test)


from sklearn import linear_model

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

Y_test = lm.predict(X_test)
for y_test in Y_test:
    print(round(y_test[0], 2))
