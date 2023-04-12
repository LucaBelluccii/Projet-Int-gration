import numpy as np
import tkinter as tk
import math
"""
RELU : rectification linéaire unitaire

envoie les éléments négatifs d'une liste sur 0
"""
def relu(x):
    return np.maximum(x, 0)


"""
Dérivée de RELU

envoie les éléments sur 0 si négatifs ou 1 si positifs
"""
def relu_derivative(x):
    return x>0


"""
réduit la magnitude du vecteur x a 1
transforme tout les éléments de x en pourcentages
"""
def softmax(x):
    temp = x - np.max(x)
    temp = np.exp(temp) / sum(np.exp(temp))
    return temp

"""
crée une liste de 0 et change l'élément a index Y pour 1 ex: 2-> [0,0,1,0,0,0,0,0,0,0]
"""
def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, 10))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

"""
retourne les listes de output du réseau en nombres ex: [0,0,1,0,0,0,0,0,0,0] -> 2
"""
def get_predictions(output):
    return np.argmax(output, 0)



"""
retourne le pourcentage de précision du réseau selon ses prédictions et les réponses attendues
"""
def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size


"""
descente de gradient
applique des dérivées trouvées par backprop sur les poids et biais du réseau
"""
def gradient_descent(network,x,y,alpha,batch_size=0):
    delta_biases, delta_weights = network.backprop(x,y)
    for i in range(len(network.biases)):
        network.weights[i] = network.weights[i] - alpha*delta_weights[i]
        network.biases[i] = network.biases[i] - alpha*delta_biases[i]

def stochastic_gradient_descent_mini_batch(network,x,y,alpha=0.1,batch_size=16,momentum=0.9):
        
    batches = math.ceil(y.size/batch_size)
        
    for n in range(batches):
        x_temp = x.T[n*batch_size:min((n+1)*batch_size,y.size-1)]
        x_temp = x_temp.T
        y_temp = y[n*batch_size:min((n+1)*batch_size,y.size-1)]
            
        delta_biases,delta_weights = network.backprop(x_temp,y_temp)
            
        for i in range(len(network.weights)):
                
            network.weights[i] = network.weights[i] - alpha*delta_weights[i]
            network.biases[i] = network.biases[i] - alpha*delta_biases[i]     
            
def gradient_descent_momentum(network,x,y,alpha=0.01,batch_size=16,momentum=0.9):
        
    batches = math.ceil(y.size/batch_size)
        
    for n in range(batches):
        x_temp = x.T[n*batch_size:min((n+1)*batch_size,y.size-1)]
        x_temp = x_temp.T
        y_temp = y[n*batch_size:min((n+1)*batch_size,y.size-1)]
            
        delta_biases,delta_weights = network.backprop(x_temp,y_temp)
            
        for i in range(len(network.weights)):
            network.velocity[i] = momentum*network.velocity[i] + alpha*delta_weights[i]
                
            network.weights[i] = network.weights[i] - network.velocity[i]
            network.biases[i] = network.biases[i] - alpha*delta_biases[i]      
   
def adaDelta(network,x,y,alpha=0.01,batch_size=0):
        
        
    delta_biases,delta_weights = network.backprop(x,y)
        
    for i in range(len(delta_weights)):
            network.gradient_sum_weights[i] += delta_weights[i]**2
            network.gradient_sum_biases[i] +=delta_biases[i]**2
    epsilon_weights = [np.zeros(network.gradient_sum_weights[i].shape)+0.000000000000000000000001 for i in range(len(delta_weights))]     
    epsilon_biases =  [np.zeros(network.gradient_sum_biases[i].shape)+0.000000000000000000000001 for i in range(len(delta_weights))]  
               
    learning_rate_weights = [alpha / (network.gradient_sum_weights[i]**(1/2)+epsilon_weights[i]) for i in range(len(delta_weights))]
    learning_rate_biases =  [alpha / (network.gradient_sum_biases[i]**(1/2)+epsilon_biases[i]) for i in range(len(delta_weights))]
    for i in range(len(delta_weights)):
        network.weights[i] = network.weights[i] - learning_rate_weights[i]*delta_weights[i]
        network.biases[i] = network.biases[i] - learning_rate_biases[i]*delta_biases[i]     
        
def adaDelta_batch(network,x,y,alpha=0.01,batch_size=16):
    batches = math.ceil(y.size/batch_size)
        
    for n in range(batches):
        x_temp = x.T[n*batch_size:min((n+1)*batch_size,y.size-1)]
        x_temp = x_temp.T
        y_temp = y[n*batch_size:min((n+1)*batch_size,y.size-1)]
        delta_biases,delta_weights = network.backprop(x_temp,y_temp)
        
        for i in range(len(delta_weights)):
                network.gradient_sum_weights[i] += delta_weights[i]**2
                network.gradient_sum_biases[i] +=delta_biases[i]**2
        epsilon_weights = [np.zeros(network.gradient_sum_weights[i].shape)+0.000000000000000000000001 for i in range(len(delta_weights))]     
        epsilon_biases =  [np.zeros(network.gradient_sum_biases[i].shape)+0.000000000000000000000001 for i in range(len(delta_weights))]  
               
        learning_rate_weights = [alpha / (network.gradient_sum_weights[i]**(1/2)+epsilon_weights[i]) for i in range(len(delta_weights))]
        learning_rate_biases =  [alpha / (network.gradient_sum_biases[i]**(1/2)+epsilon_biases[i]) for i in range(len(delta_weights))]
        for i in range(len(delta_weights)):
            network.weights[i] = network.weights[i] - learning_rate_weights[i]*delta_weights[i]
            network.biases[i] = network.biases[i] - learning_rate_biases[i]*delta_biases[i]
        
        
def adam(network,x,y,alpha=0.001,beta1=0.9,beta2=0.999):
    delta_biases,delta_weights = network.backprop(x,y)
        
    m_hat = []
    v_hat=[]
        
    epsilon = [np.zeros(delta_weights[i].shape)+0.000000000000000000000001 for i in range(len(delta_weights))]     
        
    for i in range(len(delta_weights)):
        network.momentum[i] = beta1*network.momentum[i] + (1-beta1)*delta_weights[i]
        network.velocity[i] = beta2*network.velocity[i] + (1-beta2)*delta_weights[i]**2
        m_hat.append(network.momentum[i]/(1-beta1))
        v_hat.append(network.velocity[i]/(1-beta2))
            
        network.weights[i] = network.weights[i] - m_hat[i]*(alpha/(v_hat[i]**(1/2)+epsilon[i]))
        
def adam_mini_batch(network,x,y,alpha=0.001,beta1=0.9,beta2=0.999,batch_size=16):
    batches = math.ceil(y.size/batch_size)
        
    for n in range(batches):
        x_temp = x.T[n*batch_size:min((n+1)*batch_size,y.size-1)]
        x_temp = x_temp.T
        y_temp = y[n*batch_size:min((n+1)*batch_size,y.size-1)]
        delta_biases,delta_weights = network.backprop(x_temp,y_temp)
        
        m_hat = []
        v_hat=[]
        
        epsilon = [np.zeros(delta_weights[i].shape)+0.000000000000000000000001 for i in range(len(delta_weights))]     
        
        for i in range(len(delta_weights)):
            network.momentum[i] = beta1*network.momentum[i] + (1-beta1)*delta_weights[i]
            network.velocity[i] = beta2*network.velocity[i] + (1-beta2)*delta_weights[i]**2
            m_hat.append(network.momentum[i]/(1-beta1))
            v_hat.append(network.velocity[i]/(1-beta2))
            
            network.weights[i] = network.weights[i] - m_hat[i]*(alpha/(v_hat[i]**(1/2)+epsilon[i]))
            network.biases[i] = network.biases[i] - alpha*delta_biases[i]
        

def show(network, width, height, window):
    canvas = tk.Canvas(window, width=width, height=height, background="black")
    neuronSize = 40
    margin = 5
    xstep = (width-margin*2)/(len(network.biases))

    for i, layer in enumerate(network.weights):
        x1 = i*(xstep)+margin+neuronSize/2
        x2 = (i+1)*xstep+margin+neuronSize/2
        inputStep = (height-margin*2)/len(layer[0])
        outputStep = (height-margin*2)/len(layer)
        for j in range(len(layer[0])):
            y1 = j*inputStep+margin+neuronSize/2
            for k in range(len(layer)):
                y2 = k*outputStep+margin+neuronSize/2
                red = int(255*abs(layer[k][j]))
                canvas.create_line(x1, y1, x2, y2, fill="#C41E3A")



    for i, layer in enumerate(network.weights):
        x1 = i*(xstep)+margin
        x2 = (i+1)*xstep+margin
        inputStep = (height-margin*2)/len(layer[0])
        outputStep = (height-margin*2)/len(layer)
        for j in range(len(layer[0])):
            y1 = j*inputStep+margin
            canvas.create_oval(x1, y1, x1+neuronSize,
                               y1+neuronSize, fill="blue")
        for k in range(len(layer)):
            y1 = k*outputStep+margin
            canvas.create_oval(x2, y1, x2+neuronSize,
                               y1+neuronSize, fill="blue")
    canvas.pack()
    
def show2(network, width, height, window):
    canvas = tk.Canvas(window, width=width, height=height, background="black")
        
    neuron_counts = [len(network.weights[i][1]) for i in range(len(network.biases))]
    neuron_counts.append(len(network.weights[-1]))
    
    margin = 10
    spacing = 2
    min_size = 20
    
    neuron_size = width/(max(neuron_counts))
    
    if neuron_size<min_size:
        neuron_size = min_size
        
        max_neurons = (height-margin*2)/(neuron_size)
        max_neurons =   int(((height-margin*2) - int(max_neurons)*spacing)/neuron_size)
        
        if max_neurons%2==0:
            max_neurons-=1
        
       
        
    x_step = math.ceil((width-margin*2) /  len(neuron_counts))
    
    
        
    for i, neurons in enumerate(neuron_counts):
        x1 = i*x_step + margin
        x2 = x1+neuron_size
        
        is_oversize = True if neurons>=max_neurons else False
        
        y_start = margin
        
        if neurons<max_neurons:
            blanks = (max_neurons-neurons)/2
            print(neurons,blanks,max_neurons)
            y_start = margin+((neuron_size+spacing)*blanks)
        
        for j in range(min(max_neurons,neurons)):
            
            y1 = y_start + j*(neuron_size+spacing)
            
            
            
            if j!=int(max_neurons/2) or not is_oversize:
                canvas.create_oval(x1,y1,x2,y1+neuron_size,fill="red")
            else:
                dot_size = int(neuron_size/3)
                dot_x = x1 + (x2-x1)/2 - dot_size/2
                
                canvas.create_oval(dot_x,y1,dot_x+dot_size,y1+dot_size,fill="white")
                canvas.create_oval(dot_x,y1+dot_size,dot_x+dot_size,y1+dot_size*2,fill="white")
                canvas.create_oval(dot_x,y1+dot_size*2,dot_x+dot_size,y1+dot_size*3,fill="white")
            
        
    
        
        
    
    
    
    
        
    canvas.pack()