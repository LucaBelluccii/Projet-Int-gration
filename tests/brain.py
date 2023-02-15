import numpy as np
from util import *
import random as r
import copy
import tkinter as tk

# Classe des neural networks
class Network:
    # constructeur, prends une liste contenant les nombres de neurones pour chaque layer
    def __init__(self, neuronCounts):
        self.layers = []  # liste des layers
        for i in range(len(neuronCounts)-1):  # ajouter tout les layers sauf le dernier
            self.layers.append(Layer(neuronCounts[i], neuronCounts[i+1]))

    # passe une liste de données input et retourne le output du modele    
    def feedforward(self, inputs):
        outputs = self.layers[0].feedforward(inputs)    #output du premier layer
        for i in range(1, len(self.layers)):    #appliquer au reste des layers
            outputs = self.layers[i].feedforward(outputs)
        return softmax(outputs)    #appliquer softmax au outputs finaux

    def evaluate(self, xTest, yTest):
        cost = 0
        for i, test in enumerate(xTest):
            output = self.feedforward(test)
            cost += loss(output, yTest[i])
        return cost/len(xTest)
    
    def mutate(self,mutationFactor):
        for layer in self.layers:
            for i in range(len(layer.weights)):
                for j in range(len(layer.weights[i])):
                    layer.weights[i][j] = lerp(layer.weights[i][j]+layer.weights[i][j]*mutationFactor,layer.weights[i][j]-layer.weights[i][j]*mutationFactor,r.random()) 
            for i in range(len(layer.biases)):
                layer.biases[i] = lerp(layer.biases[i]+layer.biases[i]*mutationFactor,layer.biases[i]-layer.biases[i]*mutationFactor,r.random())  
    def getClone(self):
        return copy.deepcopy(self)


# Classe des Layers des réseaux
class Layer:
    # constructeur
    # args
    # inputCount -> int, nombre de inputs
    # outputCounts -> int nombre de outputs
    # activation -> string, nom de la fonction d'activation désirée
    def __init__(self, inputCount, outputCount, activation="relu"):
        self.weights = []  # liste des weights[j][i] ou i correspond au neuron input et j aux outputs
        self.biases = []  # liste des biais
        self.outputs = [] # liste de outputs
        # activation function
        self.activation = relu

        for i in range(outputCount):  # initialiser des weights aléatoires
            self.weights.append([r.random()*2-1 for j in range(inputCount)])
            
        for i in range(outputCount):  # initialiser des biais aléatoires
            self.biases.append(r.random()*5)

        # convertir les listes en numpy array
        self.weights = np.array(self.weights)
        self.biases = np.array(self.biases)

    # passe une liste input dans le layer et retourne le output
    def feedforward(self, inputs):
        # produit matriciel input*weights
        output = np.matmul(self.weights, inputs)
        output = np.add(output, self.biases)  # ajouter les biais
        # appliquer la fonction d'activation
        output = [self.activation(x) for x in output]
        
        return output


if __name__=="__main__":
    # code pour tests
    net = Network([2, 3,3, 2])
    window = tk.Tk()
    window.resizable(False, False)

    show(net, 700, 700, window)


    test = np.array([r.randint(0, 5)
                for i in range(len(net.layers[0].weights[0]))])
    print(test.shape)
    print("outputs")
    print(net.feedforward(test))


    expectedoutput = np.zeros(len(net.layers[-1].weights))
    expectedoutput[0] = 1
    print("cost")
    print(loss((net.feedforward(test)), expectedoutput))
    
    
    #backpropfinal(net,test,expectedoutput)
    print(backprop(net,test,expectedoutput))
    #print(softmax_derivative(np.array([0.95,0,0.05,0,0])))
    
    window.mainloop()
