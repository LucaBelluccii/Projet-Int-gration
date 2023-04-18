import tkinter as tk
import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import BigBauss
import util



win = tk.PanedWindow(width=1200,height=1200)

net = BigBauss.Network([2,10,459,2])
util.show2(net,800,800,win)

win.pack()
win.mainloop()