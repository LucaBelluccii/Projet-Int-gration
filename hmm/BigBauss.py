import numpy as np
import util





class Network:
    
    """
    constructeur de la classe Network
    @params
    
    neuron_counts : liste contenant les nombres de neurones de chaque étage du réseau
    activations : liste contenant les noms (en string) des fonctions d'activation de chaque étage
    optimizer : nom (en string) de l'optimisateur du réseau 
    one_hot_output  : booléen qui décide si les données Y du réseau doivent êtres encodées ou non
    """
    
    def __init__(self,neuron_counts,activations=[],optimizer=None,one_hot_output=False):
        
        
         #liste les poids de chaque étage
        self.weights = [np.random.rand(neuron_counts[i+1],neuron_counts[i])-0.5 for i in range(len(neuron_counts)-1)]

        #liste des biais de chaque étage
        self.biases = [np.random.rand(neuron_counts[i],1)-0.5 for i in range(1,len(neuron_counts))]
    
    
        if len(activations)==0:
            print("WARNING : no activation functions provided to network")
            activations = ["" for i in range(len(neuron_counts))]
    
        self.activations = []
        self.derivatives = []
        
        for i,function in enumerate(activations):
            match function:
                case "relu":    #relu
                    self.activations.append(util.relu)
                    if i!= len(activations)-1:
                        self.derivatives.append(util.relu_derivative)
                case "softmax":     #softmax
                    self.activations.append(util.softmax)
                    if i!= len(activations)-1:
                        print("WARNING : softmax can only be used on final layer in order for backpropagation to work correctly")
                        self.derivatives.append(util.relu_derivative)
                case _:     #default (relu)
                    self.activations.append(util.relu)
                    if i!= len(activations)-1:
                        self.derivatives.append(util.relu_derivative)
    
        self.optimizer = util.gradient_descent
    
        match optimizer:
            case "gradient_descent":
                self.optimizer = util.gradient_descent
            case "adam":
                self.optimizer = util.adam
            case _:
                self.optimizer = util.adam
    
        self.one_hot_output = one_hot_output
    
    """
    accepte un input X et retourne la prédiciction du réseau
    """
    def feed_forward(self,x):
        output = self.activations[0](self.weights[0].dot(x)+self.biases[0])    #premier layer
        for i in range(1,len(self.biases)-1):   #autres layers
            output = self.activations[i](self.weights[i].dot(output)+self.biases[i])
        return self.activations[-1](self.weights[-1].dot(output)+self.biases[-1])    #dernier layer 
    
    """
    rétropropagation 

    retourne les dérivées des couts par rapport aux biais et aux poids
    """
    def backprop(self,x,y):


        #trouver les Z et les A pour les calculs (similaire a feed_forward)
        z = []
        a = []

        z.append(self.weights[0].dot(x)+self.biases[0])
        a.append(self.activations[0](z[0]))

        for i in range(1,len(self.biases)-1):
            z.append(self.weights[i].dot(a[i-1])+self.biases[i])
            a.append(self.activations[i](z[i]))
        
        z.append(self.weights[-1].dot(a[-1])+self.biases[-1])
        a.append(self.activations[-1](z[-1]))

        

        #rétropropagation (trouver les pentes)

        m = len(y)  #taille de l'échantillon

        if self.one_hot_output:
            y = util.one_hot(y)  #convertir Y en liste utilisable par le réseau
        
       
        
        delta = [0 for i in range(len(self.biases))]    #initialiser la liste des deltas

        delta[-1] = a[-1] - y   #erreur du dernier étage

        for i in range(len(self.biases)-2,-1,-1):   #erreur des autres étages
            delta[i] = self.weights[i+1].T.dot(delta[i+1]) * self.derivatives[i](z[i])

        

        delta_weights = [0 for i in range(len(self.biases))]    #initialiser la liste des erreurs de poids
        delta_biases = [0 for i in range(len(self.biases))]      #initialiser la liste des erreurs de biais

        delta_biases[0] = 1/m * np.sum(delta[0])    #erreur des premiers biais
        delta_weights[0] = 1/m * delta[0].dot(x.T)  #erreur des premiers weights

        

        for i in range(1,len(self.biases)): #erreurs des autres étages
            delta_biases[i] = 1/m * np.sum(delta[i])
            delta_weights[i] = 1/m * delta[i].dot(a[i-1].T)

        return delta_biases,delta_weights

    def train(self,x,y,alpha,batch_size=0):
        if batch_size==0:
            batch_size = len(y)
        self.optimizer(self,x,y,batch_size)

