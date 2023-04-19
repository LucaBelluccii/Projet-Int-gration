import tkinter as tk
#import numpy as np
#import math
import BigBauss
import util
#import cv2

    
   
  
window = tk.PanedWindow(width=800,height=800)
#window.geometry("800x800")
network = BigBauss.Network([784,16,16,10])

canvas = tk.Canvas(window, width=800, height=800, background="black")

util.show_network(network = network,canvas = canvas,width = 800,height = 800)


window.bind("<Configure>",lambda event: util.show_network(network = network,canvas = canvas,width = window.winfo_width(),height = window.winfo_height()))

window.pack(fill="both", expand=True)
window.mainloop()