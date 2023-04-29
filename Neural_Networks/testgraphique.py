import pygame
import subprocess
import paint
import choixreseau
import test
from tkinter.messagebox import showinfo
import tkinter_messages
import util
import pickle as pkl


def bouton(xy, text, shades, screen):
    mouse = pygame.mouse.get_pos()
    if xy[0] <= mouse[0] <= xy[0]+xy[2] and xy[1] <= mouse[1] <= xy[1]+xy[3]:
        pygame.draw.rect(screen, shades[0], xy)

    else:
        pygame.draw.rect(screen, shades[1], xy)

    screen.blit(text, (xy[0]+20, xy[1]+5))



# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screenmain = pygame.display.set_mode(res)
pygame.display.set_caption("Constructeur de réseau neural")

# color
color = "#185760"
colortext="#FFFFFF"

# shades
color_light = (67, 71, 80)
color_dark = (37, 41, 50)

# stores the width of the
# screen into a variable
width = screenmain.get_width()

# stores the height of the
# screen into a variable
height = screenmain.get_height()

# font
smallfont = pygame.font.SysFont('Corbel', 35)


# Couleurs bouton
screenmain.fill(color)
shades = [color_light, color_dark]


# Menu
textquit = smallfont.render('Quitter', True, colortext)
textreseau = smallfont.render('Créer un réseau', True, colortext)
textdessin = smallfont.render('Test dessin', True, colortext)

posquit = [width/2-70, height/2+80, 140, 40]  # position du bouton quitter
posreseau = [width/2-130, height/2-80, 260, 40]  # position du bouton reseau
posdessin = [width/2-100, height/2, 200, 40]  # position du bouton dessin

#helps
texthelpmenu=smallfont.render('?', True, colortext)
poshelpmenu=[width*7/8, height*7/8, 50, 40]
# retourMenu
textretour=smallfont.render('Retour', True, colortext)
posretour = [width/2-70, height/2+80, 140, 40]

# Reseau
textentrainer=smallfont.render('Entrainer le réseau', True, colortext)
textcreer=smallfont.render('Créer les composantes', True, colortext)
textvoirgraph=smallfont.render('Afficher le réseau', True, colortext)

posentrainer = [width/2-150, height/2, 300, 40]
poscreer= [width/2-180, height/2-160, 360, 40]
posvoirgraph = [width/2-140, height/2-80, 280, 40]

# Dessin
textfichier=smallfont.render('Modifier image', True, colortext)
texttest1=smallfont.render('Test réseau utilisateur', True, colortext)
texttest2=smallfont.render('Test réseau préentrainé', True, colortext)

posfichier=[width/2-130, height/2-160, 260, 40]
postest1=[width/2-174, height/2, 350, 40]
postest2=[width/2-185, height/2-80, 370, 40]

dessin = False
reseau = False
menu = True

while (True):

	while (menu):

		bouton(posquit, textquit, shades, screenmain)
		bouton(posreseau, textreseau, shades, screenmain)
		bouton(posdessin, textdessin, shades, screenmain)
		bouton(poshelpmenu,texthelpmenu,shades,screenmain)
    	# stores the (x,y) coordinates into
		# the variable as a tuple
		mouse = pygame.mouse.get_pos()

		for ev in pygame.event.get():

			if ev.type == pygame.QUIT:
				quit()
				
			# checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:

				# if the mouse is clicked on the
				# button the game is terminated
				if posquit[0] <= mouse[0] <= posquit[0]+posquit[2] and posquit[1] <= mouse[1] <= posquit[1]+posquit[3]:
					quit()
				elif posdessin[0] <= mouse[0] <= posdessin[0]+posdessin[2] and posdessin[1] <= mouse[1] <= posdessin[1]+posdessin[3]:
					dessin = True
					menu = False
					screenmain.fill(color)
     
				elif poshelpmenu[0] <= mouse[0] <= poshelpmenu[0]+poshelpmenu[2] and poshelpmenu[1] <= mouse[1] <= poshelpmenu[1]+poshelpmenu[3]:
					tkinter_messages.show_info_box(1)
			elif ev.type == pygame.MOUSEBUTTONUP:
					if posreseau[0] <= mouse[0] <= posreseau[0]+posreseau[2] and posreseau[1] <= mouse[1] <= posreseau[1]+posreseau[3]:
						reseau = True
						menu = False
						screenmain.fill(color)
     
 
    	# updates the frames of the game
		pygame.display.update()

	while dessin:
		bouton(posfichier, textfichier, shades, screenmain)
		bouton(posretour,textretour,shades,screenmain)
		bouton(postest1,texttest1,shades,screenmain)
		bouton(postest2,texttest2,shades,screenmain)
		bouton(poshelpmenu,texthelpmenu,shades,screenmain)
		mouse = pygame.mouse.get_pos()
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				quit()
				
			if ev.type == pygame.MOUSEBUTTONDOWN:
			
				if posretour[0] <= mouse[0] <= posretour[0]+posretour[2] and posretour[1] <= mouse[1] <= posretour[1]+posretour[3]:
						menu=True
						dessin=False
						screenmain.fill(color)
				elif posfichier[0] <= mouse[0] <= posfichier[0]+posfichier[2] and posfichier[1] <= mouse[1] <= posfichier[1]+posfichier[3]:
					subprocess.call(['mspaint', 'image.png'])
				elif postest1[0] <= mouse[0] <= postest1[0]+postest1[2] and postest1[1] <= mouse[1] <= postest1[1]+postest1[3]:
					paint.run(1)
				elif postest2[0] <= mouse[0] <= postest2[0]+postest2[2] and postest2[1] <= mouse[1] <= postest2[1]+postest2[3]:
					paint.run(2)
				elif poshelpmenu[0] <= mouse[0] <= poshelpmenu[0]+poshelpmenu[2] and poshelpmenu[1] <= mouse[1] <= poshelpmenu[1]+poshelpmenu[3]:
					tkinter_messages.show_info_box(2)
					
				
		

		pygame.display.update()

	type=""
	nblayers=0
	nbneuronnes=0
	network =pkl.load(open("big_bauss.pkl","rb"))
	activation =0
	while reseau:
     
		
  
		bouton(posretour, textretour, shades, screenmain)
		bouton(posentrainer,textentrainer,shades,screenmain)
		bouton(poscreer,textcreer,shades,screenmain)
		bouton(poshelpmenu,texthelpmenu,shades,screenmain)
		bouton(posvoirgraph,textvoirgraph,shades,screenmain)

		mouse = pygame.mouse.get_pos()
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				quit()
				
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
				if posretour[0] <= mouse[0] <= posretour[0]+posretour[2] and posretour[1] <= mouse[1] <= posretour[1]+posretour[3]:
						menu=True
						reseau=False
						screenmain.fill(color)
				elif poscreer[0] <= mouse[0] <= poscreer[0]+poscreer[2] and poscreer[1] <= mouse[1] <= poscreer[1]+poscreer[3]:
					type,nbneuronnes=choixreseau.getinfo()
					if nbneuronnes != 0:
						network = test.init_reseau(type,nbneuronnes)
				elif posentrainer[0] <= mouse[0] <= posentrainer[0]+posentrainer[2] and posentrainer[1] <= mouse[1] <= posentrainer[1]+posentrainer[3]:
					test.run(network)
				elif posvoirgraph[0] <= mouse[0] <= posvoirgraph[0]+posvoirgraph[2] and posvoirgraph[1] <= mouse[1] <= posvoirgraph[1]+posvoirgraph[3]:
					util.lauch_visualisation(network)
     
				elif poshelpmenu[0] <= mouse[0] <= poshelpmenu[0]+poshelpmenu[2] and poshelpmenu[1] <= mouse[1] <= poshelpmenu[1]+poshelpmenu[3]:
					tkinter_messages.show_info_box(3)				
		pygame.display.update()
