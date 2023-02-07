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
           
        #self.layers.append(Layer(neuronCounts[-1],neuronCounts[-1]))    #ajouter le dernier layer
    def feedforward(self,inputs):
        outputs = self.layers[0].feedforward(inputs)
        for i in range(1,len(self.layers)):
            outputs = self.layers[i].feedforward(outputs)
        return util.softmax(outputs)
    def evaluate(self,xTest,yTest):
        cost = 0
        for i,test in enumerate(xTest):
            output = self.feedforward(test)
            cost += util.costfonction(output,yTest[i])
        return cost
    
    
#Classe des Layers des réseaux
class Layer:
    #constructeur
    #args
    #neuronCount -> int, nombre de neurones du layer
    #outputs -> int nombre de neurones du prochain layer
    #activation -> string, nom de la fonction d'activation désirée
    def __init__(self,inputCount,outputCount,activation="relu"):
        self.weights = []   #liste des weights[j][i] ou i correspond au neuron input et j aux outputs
        self.biases = []    #liste des biais
        
        #activation function
        self.activation = util.relu
        
        for i in range(outputCount):    #initialiser des weights aléatoires
            self.weights.append([r.random()*2-1 for j in range(inputCount)])
        for i in range(outputCount):    #initialiser des biais aléatoires
            self.biases.append(r.randint(0,5))
        
        #convertir les listes en numpy array
        self.weights = np.array(self.weights)   
        self.biases = np.array(self.biases)

    #passe une liste input dans le layer et retourne le output
    def feedforward(self,inputs):   
        output = np.matmul(self.weights,inputs) #produit matriciel input*weights
        output = np.add(output,self.biases) #ajouter les biais
        output = [self.activation(x) for x in output]   #appliquer la fonction d'activation
        return output       

#code pour tests
net = Network([16,32,32,4])
window = tk.Tk()
window.resizable(False,False)

util.show(net,1000,1000,window)



test = np.array([r.randint(0,5) for i in range(len(net.layers[0].weights[0]))])
print(test.shape)
print("outputs")
print(net.feedforward(test))


expectedoutput=np.zeros(len(net.layers[-1].weights))
expectedoutput[0]=1
print("cost")
print(util.costfonction((net.feedforward(test)),expectedoutput))
window.mainloop()


