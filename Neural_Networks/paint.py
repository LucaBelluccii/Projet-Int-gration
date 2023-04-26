import pickle as pkl
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter.messagebox import showinfo

def run(num):
    
    if num==1:
        network = pkl.load(open("big_bauss.pkl","rb"))
    else:
        network = pkl.load(open("max_big_bauss.pkl","rb"))
    image = cv2.imread("image.png")
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    image = np.array(image)/255

    plt.imshow(image)
    plt.show()


    image = np.reshape(image,(784,1))

    msg = f'Le réseau pense que le chiffre est: {np.argmax(network.feed_forward(image))}'
    showinfo(title='Prédiction du réseau', message=msg)