import brain
import pickle as pkl
import cv2
import matplotlib.pyplot as plt
import numpy as np

def run():
    
    network = pkl.load(open("big_bauss.pkl","rb"))


    image = cv2.imread("image.png")
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    image = np.array(image)/255

    plt.imshow(image)
    plt.show()


    image = np.reshape(image,(784,1))

    print(np.argmax(network.feed_forward(image)))
