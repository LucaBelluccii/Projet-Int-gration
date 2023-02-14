import numpy as np
import math as m
from tkinter import *
import decimal

#fonction d'activation 
#retourne x si x>0 sinon 0
def relu(x):
    return max(0,x)

#convertir des valeurs rgb en hexadécimal
def rgb2hex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

def lerp(a,b,t):
    return a+t*(b-a)
    
#affiche le network dans une fenetre tkinter
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
def softmax(output):
    output -= np.max(output)
    output = np.exp(output)
    output = output/np.sum(output)
    return output

#final cost fonction
def loss(output,expectedoutput):
    
    tot=0
    for i in range(len(output)):
        tot+=(((output[i])-(expectedoutput[i]))**(2))
        
    return tot

#backprop
def backpropfinal(network,x,y):
    # goal: dCost/dWeight
    #   dCost/dWeight=dZ/dWeight * dRelu/dZ * dCost/dRelu
    #
    # a:output y: expected output w: weight b: bias
    #
    # ////////////
    #
    # dCost/dRelu = 2(a(l)-y)
    #
    # ////////////Z=w(l)a(l-1) + b(l)
    #
    # dRelu/dZ = 1
    #
    # ////////////
    #
    # dZ/dWeight = a(l-1)
    #
    # ////////////
    # 
    # dCost/dWeight= a(l-1) * 2(a(l)-y)
    
    #premiere derive
    a=[]
    output=network.layers[0].feedfoward(x)
    a.append(output)
    for i in range(1,len(network.layers)):
        output=network.layers[i].feedfoward(output)
        a.append(output)     

    a[-1]=softmax(a[-1])
    
    a=np.array(a)
    y=np.array(y)
    
    deriveout=a[-2]*2(a[-1]-y)
    
    # goal: dCost/dWeightx
    #   dCost/dWeightx= x fois /(dZ/dWeightx dRelu/dZ * dWeight/dRelu)/ * dZ/dWeight * dRelu/dZ * dCost/dRelu
    #
    #   dWeight/dRelu = a(l-x-1) * 1 *
    #
    #
    
    #next derive
