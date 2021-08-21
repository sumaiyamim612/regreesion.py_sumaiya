from numpy.lib.npyio import load
import numpy as np
import math
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from regression import Regression
from loss import rmse ,sse


iris = load_iris()
# We will use sepal length to predict sepal width
X = iris.data[:, 0].reshape(-1, 1)
Y = iris.data[:, 1].reshape(-1,1)
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size = 0.2)
print(X_test.shape) 
print(y_test.shape)
print(X_train.shape)
print(y_train.shape)
#TODO Perform a linear regression using sklearn and calculate training rmse.
# Use the SGDRegressor and only select set learning rate and epochs.
sgd = SGDRegressor(max_iter= 100, learning_rate= 'constant', eta0= 0.001)
sgd.fit(X_train, y_train)

y_pred = sgd.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
prev_rmse = math. sqrt(mse)
print("Previous model " + str(prev_rmse))

#TODO Perform a linear regression using your code and calculate training rmse.

reg = Regression(epochs=100, learning_rate=0.0001)
reg.fit(X_train, y_train)
print(reg._weights['W'].shape)
reg.pred = reg.predict(X_test)

print(y_test.shape)

reg_rmse =reg.score(y_test, reg.pred)
print('rmse class', str(reg_rmse))
