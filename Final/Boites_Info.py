import tkinter as tk
import tkinter.font as font


def show_info_box(choix):
    root = tk.Tk()
    root.geometry('500x400')
    
   
    
    titre = "Informations"
    
    root.title(titre)
    
    match choix:
        case 1:
            contenu = [["Créer un réseau:","   -Permet de créer des réseaux et de les entrainer"],
                      ["Test dessin:","   -Permet de tester le réseau sur des nombres dessinées à la main"],
                      ["Quitter","   -Quitte l'application duh"]]
    
        case 2:
            contenu = [["Modifier image:","   -Permet à l'utilisateur de changer l'image à indentifier \n(l'image doit être font noir avec un chiffre en blanc)"],
                      ["Test réseau préentrainé:","   -Identifie l'image avec le réseau préentrainé"],
                      ["Test réseau utilisateur:","   -Identifie l'image avec le réseau créé par l'utilisateur"],
                      ["Retourner","   -Retourne au menu duh"]]
        case 3:
            contenu = [["Créer les composantes:","   -Permet à l'utilisateur de choisir la structure du réseau neural à \nentrainer"],
                      ["Afficher le réseau:","   -Montre l'allure du réseau avec des connections entres neuronnes \n(rouge: poid négatif / vert: poid positif)"],
                      ["Entrainer le réseau:","   -Permet à l'utilisateur... d'entrainer le réseau"],
                      ["Retourner","   -Retourne au menu duh"]]
    for i,cont in enumerate(contenu):
        text = tk.Label(root,text = cont[0],font=("arial black",20,"underline"),anchor='w')
        text.pack(fill="both")
        text = tk.Label(root,text = cont[1],font=("cambria",12),anchor='w')
        text.pack(fill="both")
       
        
    
    root.mainloop()