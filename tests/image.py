import brain
import util

import tkinter as tk


win = tk.PanedWindow(width=400,height=400)

net = brain.Network([4,3,3])
util.show(net,400,400,win)

win.pack()
win.mainloop()