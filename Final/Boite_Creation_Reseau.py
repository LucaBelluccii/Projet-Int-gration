import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

############################################################
"""
Fichier responsable de la boite de création de réseau
"""
############################################################


"""
retourne les informations de création du réseau
"""
def getinfo():
    
    
    loop()
   
    return(typeres,nbneuronne.get())


"""
Boite de sélection
"""
def loop():
    global root
    global nblayer
    global nbneuronne
    global typeres
    
    root= tk.Tk()
    root.geometry("300x330")
    root.resizable(False, False)
    root.title('Choix du réseau neural')
    nblayer = tk.StringVar()
    nbneuronne = tk.StringVar()
    
    def login_clicked():
        global typeres
        typeres = type_entry.selection_get()
        root.destroy()
        
            
        msg = f'Vous avez choisi: {typeres} avec un réseau de configuration 784,{nbneuronne.get()},10'
        showinfo(title='Information', message=msg)
        
    # frame
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10, fill='x', expand=True)


    # type
    type_label = ttk.Label(frame, text="Optimisateur:")
    type_label.pack(fill='x', expand=True)

    type_entry = tk.Listbox(frame, selectmode="single")
    type_entry.pack(expand=True, fill="both")

    x = ["gradient descent", "gradient descent mini batch", "gradient descent momentum", "adadelta", "adadelta mini batch", "adam", "adam mini batch"]


    for each_item in range(len(x)):
        type_entry.insert("end", x[each_item])

    type_entry.selection_set(0)
    typeres = type_entry.selection_get()
    
    
    # nbneurones
    nbneuronnes_label = ttk.Label(frame, text="Nombre de neuronnes par layer:")
    nbneuronnes_label.pack(fill='x', expand=True)

    nbneuronnes_entry = ttk.Entry(frame, textvariable=nbneuronne)
    nbneuronnes_entry.pack(fill='x', expand=True)

     #ok button
    ok_button = ttk.Button(frame, text="OK", command=login_clicked)
    ok_button.pack(fill='x', expand=True, pady=10)

    
    
    root.mainloop()
    
        

    