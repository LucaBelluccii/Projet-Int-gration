import numpy as np
import util
import random as r

import tkinter as tk

class Network:
    def __init__(self,neuronCounts):
        self.layers = []
        for i in range(len(neuronCounts)-1):
            self.layers.append(Layer(neuronCounts[i],neuronCounts[i+1]))
            print(self.layers[i].biases)
        self.layers.append(Layer(neuronCounts[-1],neuronCounts[-1]))
class Layer:
    def __init__(self,neuronCount,outputs,activation="relu"):
        self.weights = []
        self.biases = []
        
        #activation function
        self.activation = util.relu
        
        
        for i in range(neuronCount):
            self.weights.append([r.random()*2-1 for j in range(outputs)])
        for i in range(neuronCount):
            self.biases.append(r.randint(0,5))



net = Network([5,10,10])
window = tk.Tk()
window.resizable(False,False)

util.showNetwork(net,1000,1000,window)



window.mainloop()


