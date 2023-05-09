import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from BigBauss import *
import tkinter as tk
import math
from tkinter.messagebox import showwarning


"""
Fichier pour l'initialisation et test d'un réseau 

Utilisé par application

"""


def init_reseau(type,nbneuronnes):
    
    #nettoyer les parametres d'utilisateur
    nbneuronnes = nbneuronnes.replace(".",",")
    nbneuronnes = nbneuronnes.replace(" ",",")
    nbneuronnes = nbneuronnes.replace("/",",")
    
    #réseau par défaut
    network = Network([784,16,16,10],optimizer=type)
    
    #essaie de créer le réseau selon les parametres d'utilisateur
    try:
        neuron_counts = [int(num) for num in (nbneuronnes.split(","))]
        if not 0 in neuron_counts and not 1 in neuron_counts:  
            neuron_counts.insert(0,784)
        neuron_counts.append(10)
        network = Network(neuron_counts,optimizer=type)
        network.feed_forward(np.random.randn(784,1))
    except:
        network = Network([784,16,16,10],optimizer=type)
        showwarning(title="you dun messed up",message="réseau invalide, structure changée pour la valeur par défaut (784,16,16,10)")
    
    return network

#teste le réseau
def run(network):
    data = pd.read_csv('Final/train.csv') #lire les données avec pandas (sourcée de Kaggle)
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

    #liste de points pour graphe
    x_plot=[]
    y_plot=[]
    
    
    #window pour get nombre de cycles
    global num
    num = 1
    root= tk.Tk()
    root.title ("Nombre de cycles")
    canvas1 = tk.Canvas(root, width=300, height=150)
    canvas1.pack()

    entry1 = tk.Entry(root) 
    
    canvas1.create_window(150, 60, window=entry1)
    
    def get_num():  
        global num 
        try:
            num= abs(math.floor(float(entry1.get())))
        except:
            showwarning(title="HEY!!",message="spa un chiffre ça :(")
            num=1
        root.destroy()
    
    button1 = tk.Button(text='   OK   ', command=get_num)
    canvas1.create_window(150, 80, window=button1)
        
    
    root.mainloop()
    
    
    #entrainement du réseau
    
    print("Précision initiale : ",util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test),"%")
    for n in range(num+1):   #cycles d'entrainement
        network.train(x = x_train,y = y_train)   #entrainer le réseau avec un facteur alpha de 0.1
        if(n%1)==0:
            x_plot.append(n)
            y_plot.append(util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test))
    
        if n%10==0:     #afficher les résultats tout les 10 cycles
            print("Epoch : ",(n+1), " , accuracy = ",util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test),"%")
    print("Précision finale : ",util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test),"%")
    pkl.dump(network,open("big_bauss.pkl","wb"))
    plt.plot(x_plot,y_plot)
    plt.show()
    
