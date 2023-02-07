import numpy as np
import util
import random as r

import tkinter as tk

#Classe des neural networks
class Network:
    #constructeur, prends une liste contenant les nombres de neurones pour chaque layer
    def __init__(self,neuronCounts):
        self.layers = []    #liste des layers
        for i in range(len(neuronCounts)-1):    #ajouter tout les layers sauf le dernier
            self.layers.append(Layer(neuronCounts[i],neuronCounts[i+1]))
           
        self.layers.append(Layer(neuronCounts[-1],neuronCounts[-1]))    #ajouter le dernier layer
    
    
#Classe des Layers des réseaux
class Layer:
    #constructeur
    #args
    #neuronCount -> int, nombre de neurones du layer
    #outputs -> int nombre de neurones du prochain layer
    #activation -> string, nom de la fonction d'activation désirée
    def __init__(self,neuronCount,outputs,activation="relu"):
        self.weights = []   #liste des weights[i][j] ou i correspond au neuron input et j aux outputs
        self.biases = []    #liste des biais
        
        #activation function
        self.activation = util.relu
        
        for i in range(neuronCount):    #initialiser des weights aléatoires
            self.weights.append([r.random()*2-1 for j in range(outputs)])
        for i in range(neuronCount):    #initialiser des biais aléatoires
            self.biases.append(r.randint(0,5))

    #passe une liste input dans le layer et retourne le output
    def feedforward(self,inputs):   
        outputs = np.zeros(len(self.weights[0]))    #liste de 0
        for i,input in enumerate(inputs):   #pour chaque input
            input -= self.biases[i]     #ajouter (soustraire) le biais du neuron au input
            input = self.activation(input)  #appliquer la fonction d'activation
            for j in range(len(outputs)):     #ajouter la valeur du neuron*les poids correspndant aux outputs
                outputs[j]+= input*self.weights[i][j]
        return outputs  #retourne les outputs
                

#code pour tests
net = Network([16,32,32,16])
window = tk.Tk()
window.resizable(False,False)

util.showNetwork(net,1000,1000,window)

test = [r.randint(0,5) for i in range(16)]
print("original")
print(util.feedforward(net,test))
print("norm")
print(util.normalise(util.feedforward(net,test)))
expectedoutput=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print("cost")
print(util.costfonction(util.normalise(util.feedforward(net,test)),expectedoutput))
window.mainloop()


