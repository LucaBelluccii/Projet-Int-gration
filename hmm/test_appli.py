import tkinter as tk
import numpy as np
import math
import BigBauss
import util
import cv2

    
   
  
window = tk.Tk()
window.geometry("800x800")
network = BigBauss.Network([784,16,16,10])
util.show_network(network,800,800,window)


#window.bind("<Configure>",lambda event: util.show_network(network,window.winfo_width(),window.winfo_height(),window))

#window.pack()
window.mainloop()