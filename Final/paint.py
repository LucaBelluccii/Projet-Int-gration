import pickle as pkl
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter.messagebox import showinfo
import math

"""
Donne la prédiction du réseau pour une image (image.png)

L'image peut être éditée dans paint la taille doit demeurer 28x28 pixels
"""


def run(num):
    
    #charger le réseau 
    
    if num==1:
        network = pkl.load(open("big_bauss.pkl","rb"))
    else:
        network = pkl.load(open("max_big_bauss.pkl","rb"))
        
        
    #lire l'image avec opencv
    image = cv2.imread("image.png")
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    image = np.array(image)/255
    
    
    #centrer le chiffre dans l'image
    
    #coordonnées du chiffre
    ytop=0
    ybot=0
    xdroite=0
    xgauche=0
    
    #trouver les coordonnées
    marker=False
    #top & #bot
    for y in range(len(image)):
        for x in range(len(image)):
            if (image[x][y]>0):
                if marker==False:
                    xgauche=y
                    
                    marker=True
                else:
                    xdroite=y
    marker=False
    #droite & #gauche
    for x in range(len(image)):
        for y in range(len(image)):
            if (image[x][y]>0):
                if marker==False:
                    ytop=x
                    marker=True
                else:
                    ybot=x
    
    #trouver le milieu
    mid=[math.ceil(xgauche+(xdroite-xgauche)/2),math.ceil(ytop+(ybot-ytop)/2)]
    x=mid[0]-14
    y=mid[1]-14
    
    #déplacer l'image (ajouter et enlever des lignes de pixels noirs)
    
    if y>0:
        image=image[y:28]
        for i in range(y):
            image=np.vstack([image,[0 for j in range(28)]])
        
    else:
        image=image[0:28+y]
        for i in range(abs(y)):
            image=np.vstack([[0 for j in range(28)],image])
    image=image.T
    
    
    if x>0:
        image=image[x:28]
        for i in range(x):
            image=np.vstack([image,[0 for j in range(28)]])
        
    else:
        image=image[0:28+x]
        for i in range(abs(x)):
            
            image=np.vstack([[0 for j in range(28)],image])
    image=image.T
    
    #afficher l'image
    
    plt.imshow(image)
    plt.show()

    #"aplatir" l'image pour le réseau
    image = np.reshape(image,(784,1))

    #afficher la prédiction
    msg = f'Le réseau pense que le chiffre est: {np.argmax(network.feed_forward(image))}'
    showinfo(title='Prédiction du réseau', message=msg)