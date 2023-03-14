import numpy as np

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
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
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
Classe des réseaux 
Programmés en objet afin d'être sérialisable
"""
class Network:
    """
    Constructeur

    neuron_counts : liste des nombres de neurones de chaque étage

    les valeurs de poids et biais sont instanciées avec des nombres aléatoires
    """
    def __init__(self,neuron_counts):
        #liste les poids de chaque étage
        self.weights = [np.random.rand(neuron_counts[i+1],neuron_counts[i])-0.5 for i in range(len(neuron_counts)-1)]

        #liste des biais de chaque étage
        self.biases = [np.random.rand(neuron_counts[i],1)-0.5 for i in range(1,len(neuron_counts))]


    """
    accepte un input X et retourne la prédiciction du réseau
    """
    def feed_forward(self,x):

        output = relu(self.weights[0].dot(x)+self.biases[0])    #premier layer
        for i in range(1,len(self.biases)-1):   #autres layers
            output = relu(self.weights[i].dot(output)+self.biases[i])
        return softmax(self.weights[-1].dot(output)+self.biases[-1])    #dernier layer utilise softmax
    
    """
    rétropropagation 

    retourne les dérivées des couts par rapport aux biais et aux poids
    """
    def backprop(self,x,y):


        #trouver les Z et les A pour les calculs (similaire a feed_forward)
        z = []
        a = []

        z.append(self.weights[0].dot(x)+self.biases[0])
        a.append(relu(z[0]))

        for i in range(1,len(self.biases)-1):
            z.append(self.weights[i].dot(a[i-1])+self.biases[i])
            a.append(relu(z[i]))
        
        z.append(self.weights[-1].dot(a[-1])+self.biases[-1])
        a.append(softmax(z[-1]))

        

        #rétropropagation (trouver les pentes)

        m = len(y)  #taille de l'échantillon

        y = one_hot(y)  #convertir Y en liste utilisable par le réseau


        
        delta = [0 for i in range(len(self.biases))]    #initialiser la liste des deltas

        delta[-1] = a[-1] - y   #erreur du dernier étage

        for i in range(len(self.biases)-2,-1,-1):   #erreur des autres étages
            delta[i] = self.weights[i+1].T.dot(delta[i+1]) * relu_derivative(z[i])

        

        delta_weights = [0 for i in range(len(self.biases))]    #initialiser la liste des erreurs de poids
        delta_biases = [0 for i in range(len(self.biases))]      #initialiser la liste des erreurs de biais

        delta_biases[0] = 1/m * np.sum(delta[0])    #erreur des premiers biais
        delta_weights[0] = 1/m * delta[0].dot(x.T)  #erreur des premiers weights

        

        for i in range(1,len(self.biases)): #erreurs des autres étages
            delta_biases[i] = 1/m * np.sum(delta[i])
            delta_weights[i] = 1/m * delta[i].dot(a[i-1].T)

        return delta_biases,delta_weights
    
    """
    descente de gradient
    applique des dérivées trouvées par backprop sur les poids et biais du réseau
    """
    def gradient_descent(self,x,y,alpha):
        delta_biases, delta_weights = self.backprop(x,y)
        for i in range(len(self.biases)):
            self.weights[i] = self.weights[i] - alpha*delta_weights[i]
            self.biases[i] = self.biases[i] - alpha*delta_biases[i]



