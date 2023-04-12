import numpy as np
import math as m
from tkinter import *
import decimal

# fonction d'activation
# retourne x si x>0 sinon 0


def relu(x):
    return max(0, x)

# convertir des valeurs rgb en hexadécimal


def rgb2hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def lerp(a, b, t):
    return a+t*(b-a)

# affiche le network dans une fenetre tkinter


def show(network, width, height, window):
    canvas = Canvas(window, width=width, height=height, background="black")
    neuronSize = 10
    margin = 20
    xstep = (width-margin*2)/(len(network.layers))

    for i, layer in enumerate(network.layers):
        x1 = i*(xstep)+margin+neuronSize/2
        x2 = (i+1)*xstep+margin+neuronSize/2
        inputStep = (height-margin*2)/len(layer.weights[0])
        outputStep = (height-margin*2)/len(layer.weights)
        for j in range(len(layer.weights[0])):
            y1 = j*inputStep+margin+neuronSize/2
            for k in range(len(layer.weights)):
                y2 = k*outputStep+margin+neuronSize/2
                red = int(255*abs(layer.weights[k][j]))
                canvas.create_line(x1, y1, x2, y2, fill="#C41E3A")

    for i, layer in enumerate(network.layers):
        x1 = i*(xstep)+margin
        x2 = (i+1)*xstep+margin
        inputStep = (height-margin*2)/len(layer.weights[0])
        outputStep = (height-margin*2)/len(layer.weights)
        for j in range(len(layer.weights[0])):
            y1 = j*inputStep+margin
            canvas.create_oval(x1, y1, x1+neuronSize,
                               y1+neuronSize, fill="blue")
        for k in range(len(layer.weights)):
            y1 = k*outputStep+margin
            canvas.create_oval(x2, y1, x2+neuronSize,
                               y1+neuronSize, fill="blue")
    canvas.pack()


# Somme normalisé pour le output
def softmax(output):
    output -= np.max(output)
    output = np.exp(output)
    output = output/np.sum(output)
    return output

# final cost fonction


def loss(output, expectedoutput):

    tot = 0
    for i in range(len(output)):
        tot += (((output[i])-(expectedoutput[i]))**(2))

    return tot/2

# backprop


def backpropfinal(network, x, y):

    a = []
    z = []

    output = network.layers[0].feedforward(x)

    a.append(np.array(output))
    for i in range(1, len(network.layers)):
        output = network.layers[i].feedforward(output)
        a.append(np.array(output))

    a[-1] = softmax(np.array(a[-1]))

    y = np.array(y)

    variations = []

    ogerror = a[-1]-y
    variations.append(ogerror)
    for i in reversed(range(0, len(network.layers)-1)):
        weights = np.transpose(network.layers[i+1].weights)
        if (i == len(network.layers)-1):
            variations.append((ogerror)*softmax_derivative(ogerror))
        else:
            variations.append(
                (weights@variations[len(variations)-1])*relu_derivative(a[len(variations)-1]))

    # print('l3')
    # print(a[2])
    # print('vars')
    # print(variations[0])
    # print('mult')
    # print(a[2]*variations[0])

    weightsvar = []  # variation pour weights
    biasesvar = []  # variation pour biases

    i = len(variations)-1

    for num in a:
        weightsvar.append(np.matmul(variations[i],np.transpose(num)))  # ajoute les weights var
        biasesvar.append(variations[i])  # réordonne les biases var
        i -= 1

    return biasesvar, weightsvar


def relu_vector(x):
    return np.array([max(0, n) for n in x])


def relu_derivative(x):
    for i, n in enumerate(x):
        x[i] = 0 if n <= 0 else 1
    return x


def softmax_derivative(x):
    x_reshape = x.reshape(-1, 1)
    return np.diagflat(x_reshape) - np.dot(x_reshape, np.transpose(x_reshape))


def evaluate(network,test_data):
    cost = 0
    for data in test_data:
        prediction = network.feedforward(data[0])
        cost += loss(prediction,data[1])
    return cost/len(test_data)


def train(network,data,batch_size,learning_rate):
    batches = m.ceil(len(data)/batch_size)
    
    for i in range(batches):
        batch = data[i*batch_size:min((i+1)*batch_size,len(data))]
        gradient_descent(network,batch,learning_rate)    

def gradient_descent(network,batch, learning_rate):

    bias_derivative = []
    weights_derivative = []

    for layer in network.layers:
        bias_derivative.append(np.array([0.0 for bias in layer.biases]))
        weights_derivative.append(np.array([0.0 for weight in (layer.weights)]))

   

    for data in batch:
        biases, weights = backpropfinal(network, data[0], data[1])
        for i, bias in enumerate(biases):
            bias_derivative[i] += bias
        for i, weight in enumerate(weights):
            weights_derivative[i] += weight

    for i, layer in enumerate(network.layers):
       
        layer.weights = np.transpose(np.transpose(layer.weights)-(weights_derivative[i]*(learning_rate/len(batch))))
        
        layer.biases = layer.biases - (bias_derivative[i]*(learning_rate/len(batch)))
    


# ajoute le backprop au biases
def addbacktobiases(net, test, expectedoutput):
    deltaarray, deltarr = (backpropfinal(net, test, expectedoutput))
    # print()
    # print()
    # print('Difbiases:')
    # print(deltaarray)

    # print()
    # print()
    # print('Newbiases:')
    for i, layer in enumerate(net.layers):
        # constante pour amplifier (a enlever lorsqu'un affectera les weights)
        layer.biases = layer.biases-deltaarray[i]*100

    # for layer in net.layers:
    #    print(layer.biases)

# ajoute le backprop au weights


def addbacktoweights(net, test, expectedoutput):
    deltaarray, deltarr = (backpropfinal(net, test, expectedoutput))

    for i, layer in enumerate(net.layers):

        # WARNING marche surement pas
        temp = np.transpose(layer.weights)

        for j in range(len(temp)):
            temp[j] = temp[j] - deltarr[i]*100
        layer.weights = np.transpose(temp.copy())

def imtodata(imagelist):
    newlist=[]
    for i in range(len(imagelist)):
        newlist.append(np.array(imagelist[i]).flatten())
    return newlist


    

def numtolist(data,net):
    converted_data = []
    for num in data:
        newlist = np.zeros(len(net.layers[-1].weights))
        
        newlist[num] = 1
        converted_data.append(newlist)
    return (converted_data)