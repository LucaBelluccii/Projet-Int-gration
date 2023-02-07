import numpy as np
import math as m
from tkinter import *


#fonction d'activation 
#retourne x si x>0 sinon 0
def relu(x):
    return max(0,x)

#convertir des valeurs rgb en hexadécimal
def rgb2hex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

#affiche un network
def showNetwork(network,width,height,window):
    canvas = Canvas(window,width = width, height = height,background="black")
    rows = len(network.layers)
    neuronDim = 5
    
    for i in range(rows-1):
        for j in range(len(network.layers[i].weights)):
            x1 = (i)*((width)/rows)+50+neuronDim/2
            y1 = (j)*((height)/len(network.layers[i].weights))+15+neuronDim/2
            x2 = (i+1)*((width)/rows)+50+neuronDim/2
            for k in range(len(network.layers[i+1].biases)):
                y2 = (k)*((height)/len(network.layers[i+1].biases))+15+neuronDim/2
                
                red = int(255*(abs(network.layers[i].weights[j][k])))
                canvas.create_line(x1,y1,x2,y2,fill =rgb2hex(red,0,0))
    
    for i in range(rows):
        for j in range(len(network.layers[i].biases)):
            x = (i)*((width)/rows)+50
            y = (j)*((height)/len(network.layers[i].biases))+15
            canvas.create_oval(x,y,x+neuronDim,y+neuronDim,fill = "blue")
    
    canvas.pack()

#passe une liste input dans le network et retourne les outputs
def feedforward(network,inputs):
    input_layer= network.layers[0]  #prendre le premier layer
    output = input_layer.feedforward(inputs)    #passer les données input dans le premier layer
    for i in range(len(network.layers)-2):  #répéter pour les autres layers
        output = network.layers[i+1].feedforward(output)
    output = [relu(x) for x in output]
    return output

#Somme normalisé pour le output
def normalise(output):
    newoutput=[]
    tot=0
    for x in output:
        tot+=m.e**x
    
    for x in output:
        newoutput.append(m.e**x/tot)
    return newoutput

#final cost fonction
def costfonction(output,expectedoutput):
    tot=0
    for i in range(len(output)-1):
        tot+=((output[i]-expectedoutput[i])**2)
        
    return tot