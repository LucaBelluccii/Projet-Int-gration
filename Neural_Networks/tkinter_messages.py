import tkinter as tk
import tkinter.font as font


def show_info_box():
    root = tk.Tk()
    root.geometry('500x400')
    
    #text = tk.Text(root,wrap='word', padx=10, pady=10)
    #text.pack(fill='both', padx=10, pady=10)
    
    titre = "Informations"
    
    contenu = [["Créer un réseau:","   -permet de créer des réseaux et de les entrainer"]]
    labels=[]
    for i,cont in enumerate(contenu):
        labels.append(tk.Label(root,text = cont[0],font=("arial black",20,"underline"),anchor='w'))
        labels[i].pack(fill="both")
        labels.append(tk.Label(root,text = cont[1],font=("cambria",12),anchor='w'))
        labels[i+1].pack(fill="both")
       
        
    
    root.mainloop()