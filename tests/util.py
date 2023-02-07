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
    neuronDim = 20
    
    for i in range(rows):
        for j in range(len(network.layers[i].weights[0])):
            x1 = (i)*((width)/rows)+50+neuronDim/2
            y1 = (j)*((height)/len(network.layers[i].weights))+15+neuronDim/2
            x2 = (i+1)*((width)/rows)+50+neuronDim/2
            for k in range(len(network.layers[i].weights)):
                y2 = (k)*((height)/len(network.layers[i].biases))+15+neuronDim/2
                
                red = int(255*(abs(network.layers[i].weights[j][k])))
                canvas.create_line(x2,y2,x1,y1,fill =rgb2hex(red,0,0))
                
    for i in range(rows):
        for j in range(len(network.layers[i].weights[0])):
            x = (i)*((width)/rows)+50
            y = (j)*((height)/len(network.layers[i].weights[0]))+15
            canvas.create_oval(x,y,x+neuronDim,y+neuronDim,fill = "blue")
    
    canvas.pack()
def show(network,width,height,window):
    canvas = Canvas(window,width = width, height = height,background="black")
    neuronSize = 10
    margin = 20
    xstep = (width-margin*2)/(len(network.layers))
    
    for i,layer in enumerate(network.layers):
        x1 = i*(xstep)+margin+neuronSize/2
        x2 = (i+1)*xstep+margin+neuronSize/2
        inputStep = (height-margin*2)/len(layer.weights[0])
        outputStep = (height-margin*2)/len(layer.weights)
        for j in range(len(layer.weights[0])):
            y1 = j*inputStep+margin+neuronSize/2
            for k in range(len(layer.weights)):
                y2 = k*outputStep+margin+neuronSize/2
                red = int(255*abs(layer.weights[k][j]))
                canvas.create_line(x1,y1,x2,y2,fill =rgb2hex(red,0,0))
                
                
    for i,layer in enumerate(network.layers):
        x1 = i*(xstep)+margin
        x2 = (i+1)*xstep+margin
        inputStep = (height-margin*2)/len(layer.weights[0])
        outputStep = (height-margin*2)/len(layer.weights)
        for j in range(len(layer.weights[0])):
            y1 = j*inputStep+margin
            canvas.create_oval(x1,y1,x1+neuronSize,y1+neuronSize,fill = "blue")
        for k in range(len(layer.weights)):
            y1 = k*outputStep+margin
            canvas.create_oval(x2,y1,x2+neuronSize,y1+neuronSize,fill = "blue")
    canvas.pack()
       

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