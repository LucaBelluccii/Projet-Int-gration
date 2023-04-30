import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from BigBauss import *
import tkinter as tk
from tkinter.messagebox import showwarning

def init_reseau(type,nbneuronnes):
    
    nbneuronnes = nbneuronnes.replace(".",",")
    nbneuronnes = nbneuronnes.replace(" ",",")
    nbneuronnes = nbneuronnes.replace("/",",")
    network = Network([784,16,16,10],optimizer=type)
    try:
        neuron_counts = [int(num) for num in (nbneuronnes.split(","))]
        if not 0 in neuron_counts and not 1 in neuron_counts:  
            neuron_counts.insert(0,784)
        neuron_counts.append(10)
        network = Network(neuron_counts,optimizer=type)
        network.feed_forward(np.random.randn(784,1))
    except:
        network = Network([784,16,16,10],optimizer=type)
        showwarning(title="you dun fucked up",message="réseau invalide, structure changée pour la valeur par défaut (784,16,16,10)")
    
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

    #new coords pour graph
    x_plot=[]
    y_plot=[]
    
    try:
    #window pour get nombre de cycles
        global num
        root= tk.Tk()

        canvas1 = tk.Canvas(root, width=400, height=300)
        canvas1.pack()

        entry1 = tk.Entry(root) 
    
        canvas1.create_window(200, 140, window=entry1)
    
        def get_num():  
            global num 
            num= int(entry1.get())
            root.destroy()
    
        button1 = tk.Button(text='Get num', command=get_num)
        canvas1.create_window(200, 180, window=button1)
        
    
        root.mainloop()
    except:
        showwarning(title="HEY!!",message="Vous devez entrer un entier :(")
        num=100
        

    print(num)

    for n in range(num):   #cycles d'entrainement
        network.train(x = x_train,y = y_train)   #entrainer le réseau avec un facteur alpha de 0.1
        if(n%1)==0:
            x_plot.append(n)
            y_plot.append(util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test))
    
        if n%10==0:     #afficher les résultats tout les 50 cycles
            print("Epoch : ",n, " , accuracy = ",util.get_accuracy(util.get_predictions(network.feed_forward(x_test)),y_test))
    pkl.dump(network,open("big_bauss.pkl","wb"))
    plt.plot(x_plot,y_plot)
    plt.show()
    
