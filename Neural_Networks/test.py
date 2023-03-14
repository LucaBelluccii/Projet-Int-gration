import numpy as np
import pandas as pd


from brain import *

data = pd.read_csv('Neural_Networks/train.csv')

data = np.array(data)

m, n = data.shape
np.random.shuffle(data)

data_test = data[0:1000].T
y_test = data_test[0]
x_test = data_test[1:n]
x_test = x_test / 255.

data_train = data[1000:m].T
y_train = data_train[0]
x_train = data_train[1:n]
x_train = x_train / 255.0


network = Network([784,32,32,10])
for n in range(1000):
    network.gradient_descent(x_train,y_train,0.1)
    if n%10==0:
        print("Epoch : ",n, " , accuracy = ",get_accuracy(get_predictions(network.feed_forward(x_test)),y_test))
