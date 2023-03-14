import numpy as np


def relu(x):
    return np.maximum(x, 0)

def relu_derivative(x):
    return x>0

def softmax(x):
    temp = x - np.max(x)
    temp = np.exp(temp) / sum(np.exp(temp))
    return temp

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def get_predictions(output):
    return np.argmax(output, 0)

def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size



class Network:
    def __init__(self,neuron_counts):
        self.weights = [np.random.rand(neuron_counts[i+1],neuron_counts[i])-0.5 for i in range(len(neuron_counts)-1)]
        self.biases = [np.random.rand(neuron_counts[i],1)-0.5 for i in range(1,len(neuron_counts))]

    def feed_forward(self,x):
        output = relu(self.weights[0].dot(x)+self.biases[0])
        for i in range(1,len(self.biases)-1):
            output = relu(self.weights[i].dot(output)+self.biases[i])
        return softmax(self.weights[-1].dot(output)+self.biases[-1])
    
    def backprop(self,x,y):


        #forward pass
        z = []
        a = []

        z.append(self.weights[0].dot(x)+self.biases[0])
        a.append(relu(z[0]))

        for i in range(1,len(self.biases)-1):
            z.append(self.weights[i].dot(a[i-1])+self.biases[i])
            a.append(relu(z[i]))
        
        z.append(self.weights[-1].dot(a[-1])+self.biases[-1])
        a.append(softmax(z[-1]))

        #backwards pass

        m = len(y)

        y = one_hot(y)


        #trouver les deltas
        delta = [0 for i in range(len(self.biases))]

        delta[-1] = a[-1] - y

        for i in range(len(self.biases)-2,-1,-1):
            delta[i] = self.weights[i+1].T.dot(delta[i+1]) * relu_derivative(z[i])

        #dérivées de poids et biais

        delta_weights = [0 for i in range(len(self.biases))]
        delta_biases = [0 for i in range(len(self.biases))]

        delta_biases[0] = 1/m * np.sum(delta[0])
        delta_weights[0] = 1/m * delta[0].dot(x.T)

        

        for i in range(1,len(self.biases)):
            delta_biases[i] = 1/m * np.sum(delta[i])
            delta_weights[i] = 1/m * delta[i].dot(a[i-1].T)

        return delta_biases,delta_weights
    
    def gradient_descent(self,x,y,alpha):
        delta_biases, delta_weights = self.backprop(x,y)
        for i in range(len(self.biases)):
            self.weights[i] = self.weights[i] - alpha*delta_weights[i]
            self.biases[i] = self.biases[i] - alpha*delta_biases[i]



