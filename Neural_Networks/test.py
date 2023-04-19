import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from BigBauss import *
from tkinter.messagebox import showwarning

def init_reseau(type,nbneuronnes):
    
    
    network = Network([784,16,16,10],optimizer=type)
    try:
        neuron_counts = [int(num) for num in (nbneuronnes.split(","))]
        neuron_counts.insert(0,784)
        neuron_counts.append(10)
        network = Network(neuron_counts,optimizer=type)
        network.feed_forward(np.random.randn(784,1))
    except:
        network = Network([784,16,16,10],optimizer=type)
        showwarning(title="you dun fucked up",message="réseau invalide")
    
    return network


def run(network):
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
        network.train(x = x_train,y = y_train,alpha=0.001)   #entrainer le réseau avec un facteur alpha de 0.1
        if(n%1)==0:
            x_plot.append(n)
            y_plot.append(util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test))
    
        if n%10==0:     #afficher les résultats tout les 50 cycles
            print("Epoch : ",n, " , accuracy = ",util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test))
    pkl.dump(network,open("big_bauss.pkl","wb"))
    plt.plot(x_plot,y_plot)
    plt.show()