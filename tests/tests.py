from brain import *
from random import *


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



input_layer_size = 100
dataSize = 1000

xTrain,yTrain = generateData(dataSize,input_layer_size)
print("generated data")

number_of_networks = 10
structure = [input_layer_size,128,128,128,input_layer_size]
networks = [Network(structure) for i in range(number_of_networks)]
print("networks generated")



minCost = 99999
minIndex = 0
total = 0
print("evaluating gen 1...")
for i,network in enumerate(networks):
    cost = network.evaluate(xTrain,yTrain)
    total+=cost
    if cost<minCost:
        minCost = cost
        minIndex = i
average = total/number_of_networks
print("best of gen 1 : loss = ",minCost)
print("average cost = ",average)






    