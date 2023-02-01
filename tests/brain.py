import numpy as np
import util
import random as r

import tkinter as tk

class Network:
    def __init__(self,neuronCounts):
        self.layers = []
        for i in range(len(neuronCounts)-1):
            self.layers.append(Layer(neuronCounts[i],neuronCounts[i+1]))
           
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

    def feedforward(self,inputs):
        outputs = np.zeros(len(self.weights[0]))
        for i,input in enumerate(inputs):
            input -= self.biases[i]
            input = self.activation(input)
            for j in range(len(outputs)):
                outputs[j]+= input*self.weights[i][j]
        return outputs
                


net = Network([16,32,32,16])
window = tk.Tk()
window.resizable(False,False)

util.showNetwork(net,1000,1000,window)

test = [r.randint(0,5) for i in range(16)]
print(util.feedforward(net,test))
window.mainloop()


