from brain import *
from random import *
from keras.datasets import mnist
import matplotlib.pyplot as plt
import pickle as plk
def generateData(dataSize,dataLen):
    xTest = []
    yTest = []
    for i in range(dataSize):
        digit = randint(0,dataLen-1)
        xTest.append(np.zeros(dataLen))
        yTest.append(np.zeros(dataLen))
        xTest[i][digit]=1
        yTest[i][digit]=1   
    return xTest,yTest

def mutateGen(best,networks,factor):
    number = len(networks)
    networks = [best.getClone() for i in range(number)]
    for net in networks:
        net.mutate(factor)
    return networks

def evaluateGen(networks,xTrain,yTrain):
    minCost = 99999
    minIndex = 0
    total = 0
    iterations = len(xTrain)
    for i,network in enumerate(networks):
        if i%100==0:
            print(i,"/",iterations)
        cost = network.evaluate(xTrain,yTrain)
        total+=cost
        if cost<minCost:
            minCost = cost
            minIndex = i
    average = total/number_of_networks
    print("best of gen : loss = ",minCost)
    print("average cost = ",average)
    return minIndex

input_layer_size = 100
dataSize = 20

MUTATION_FACTOR = 0.1

number_of_networks = 10
structure = [784,16,16,10]
networks = [Network(structure) for i in range(number_of_networks)]

#xTrain,yTrain = generateData(dataSize,input_layer_size)
xTrain = plk.load(open("x.plk","rb"))
yTrain = plk.load(open("y.plk","rb"))



print("generated data")

epochs = input("epooches = ")

for i in range(int(epochs)):
    print("evaluating gen",(i+1))
    best = evaluateGen(networks,xTrain,yTrain)
    networks = mutateGen(networks[best],networks,MUTATION_FACTOR)
    
    

