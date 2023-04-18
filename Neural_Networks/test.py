import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from brain import *
from tkinter.messagebox import showwarning

def init_reseau(type,nblayer,nbneuronnes):
    network = Network([784,16,16,10])
    try:
        neuron_counts = [int(num) for num in (nbneuronnes.split(","))]
        print(neuron_counts)
        network = Network(neuron_counts)
        print(network.feed_forward(np.random.randn(784,1)))
    except:
        network = Network([784,16,16,10])
        showwarning(title="you dun fucked up",message="réseau invalide")
    activation = 0
    optimisers = ["gradient descent", "gradient descent mini batch", "gradient descent momentum", "adadelta", "adadelta mini batch", "adam", "adam mini batch"]
    fonctions= [gradient_descent,stochastic_gradient_descent_mini_batch, gradient_descent_momentum, adaDelta, adaDelta_batch, adam, adam_mini_batch]
    print(type)
    activation = fonctions[optimisers.index(type)]
    print(activation)
    
    return network,activation


def run(network,activation):
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

    
        
    
        
    x_plot=[]
    y_plot=[]

    for n in range(100):   #cycles d'entrainement
        activation(network = network,x = x_train,y = y_train,alpha=0.001)   #entrainer le réseau avec un facteur alpha de 0.1
        if(n%1)==0:
            x_plot.append(n)
            y_plot.append(get_accuracy(get_predictions(network.feed_forward(x_test)),y_test))
    
        if n%10==0:     #afficher les résultats tout les 50 cycles
            print("Epoch : ",n, " , accuracy = ",get_accuracy(get_predictions(network.feed_forward(x_test)),y_test))
    pkl.dump(network,open("big_bauss.pkl","wb"))
    plt.plot(x_plot,y_plot)
    plt.show()