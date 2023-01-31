import numpy as np
from tkinter import *

def relu(x):
    return max(0,x)

def showNetwork(network,width,height,window):
    canvas = Canvas(window,width = width, height = height)
    rows = len(network.layers)
    neuronDim = 20
    for i in range(rows):
        for j in range(len(network.layers[i].biases)):
            x = (i)*((width-10)/rows)
            y = (j)*((height-10)/len(network.layers[i].biases))
            canvas.create_oval(x,y,x+neuronDim,y+neuronDim)
    canvas.pack()