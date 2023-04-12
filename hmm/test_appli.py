import tkinter as tk
import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import BigBauss
import util

win = tk.PanedWindow(width=400,height=400)

net = BigBauss.Network([5,84,459,2])
util.show2(net,400,400,win)

win.pack()
win.mainloop()