import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from brain import *





data = pd.read_csv('Neural_Networks/train.csv') #lire les données avec pandas (sourcée de Kaggle)
data = np.array(data)   #convertir en liste numpy
m, n = data.shape   #dimensions des données
np.random.shuffle(data)     #mélanger
data_test = data[0:1000].T  #séparer une partie des données pour tester la précicion du réseau
y_test = data_test[0]       #séparer x et y 
x_test = data_test[1:n]
x_test = x_test / 255.0     #diviser x par 255 pour obtenir des valeurs entre 0 et 1

data_train = data[1000:m].T     #appliquer la même méthode au données d'entrainement
y_train = data_train[0]
x_train = data_train[1:n]
x_train = x_train / 255.0


network = Network([784,16,16,10])   #création du réseau


x_plot=[]
y_plot=[]

for n in range(500):   #cycles d'entrainement
    network.gradient_descent(x_train,y_train,0.9)   #entrainer le réseau avec un facteur alpha de 0.1
    if(n%5)==0:
        x_plot.append(n)
        y_plot.append(get_accuracy(get_predictions(network.feed_forward(x_test)),y_test))
    
    if n%50==0:     #afficher les résultats tout les 50 cycles
        print("Epoch : ",n, " , accuracy = ",get_accuracy(get_predictions(network.feed_forward(x_test)),y_test))
pkl.dump(network,open("big_bauss.pkl","wb"))
plt.plot(x_plot,y_plot)
plt.show()