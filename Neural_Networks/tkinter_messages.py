import tkinter as tk
import tkinter.font as font


def show_info_box():
    root = tk.Tk()
    root.geometry('500x400')
    
   
    
    titre = "Informations"
    
    root.title(titre)
    
    contenu = [["Créer un réseau:","   -Permet de créer des réseaux et de les entrainer"],
               ["Test dessin:","   -Permet de tester le réseau sur des nombres dessinées à la main"],
               ["Quitter","   -Quitte l\'application duh"]]
    
    for i,cont in enumerate(contenu):
        text = tk.Label(root,text = cont[0],font=("arial black",20,"underline"),anchor='w')
        text.pack(fill="both")
        text = tk.Label(root,text = cont[1],font=("cambria",12),anchor='w')
        text.pack(fill="both")
       
        
    
    root.mainloop()