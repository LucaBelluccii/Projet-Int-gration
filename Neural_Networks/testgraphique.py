import pygame
import subprocess
import paint
import choixreseau
import test


def bouton_quit(xy, text, shades, screen):

    # stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()

	# if mouse is hovered on a button it
	# changes to lighter shade
	if xy[0] <= mouse[0] <= xy[0]+xy[2] and xy[1] <= mouse[1] <= xy[1]+xy[3]:
		pygame.draw.rect(screen, shades[0], xy)

	else:
		pygame.draw.rect(screen, shades[1], xy)

	# superimposing the text onto our button
	screen.blit(text, (xy[0]+40, xy[1]+5))


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
# white color
color = (255, 255, 255)

# shades
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screenmain.get_width()

# stores the height of the
# screen into a variable
height = screenmain.get_height()

# font
smallfont = pygame.font.SysFont('Corbel', 35)


# Couleurs bouton
screenmain.fill((255, 255, 255))
shades = [color_light, color_dark]


# Menu
textquit = smallfont.render('Quit', True, color)
textreseau = smallfont.render('Creer un reseau', True, color)
textdessin = smallfont.render('Test dessin', True, color)

posquit = [width/2-70, height/2+80, 140, 40]  # position du bouton quitter
posreseau = [width/2-130, height/2-80, 260, 40]  # position du bouton reseau
posdessin = [width/2-100, height/2, 200, 40]  # position du bouton dessin

# retourMenu
textretour=smallfont.render('Retour', True, color)
posretour = [width/2-70, height/2+80, 140, 40]

# Reseau
textcreer=smallfont.render('Créer', True, color)
textchoisir=smallfont.render('Choisir', True, color)
textsgd=smallfont.render('stochastic_gradient_descent_mini_batch', True, color)
textsgdMB=smallfont.render('stochastic_gradient_descent_mini_batch', True, color)
textgdMo=smallfont.render('gradient_descent_momentum', True, color)
textadaD=smallfont.render('adaDelta', True, color)
textadaDMB=smallfont.render('adaDelta_mini_batch', True, color)
textadam=smallfont.render('ADAM', True, color)
textadamMB=smallfont.render('ADAM_mini_batch', True, color)

poscreer = [width/2-100, height/2, 200, 40]
poschoisir= [width/2-130, height/2-80, 260, 40]


# Dessin
textfichier=smallfont.render('Modifier image', True, color)
texttest=smallfont.render('Test', True, color)

posfichier=[width/2-130, height/2-80, 260, 40]
postest=[width/2-50, height/2, 100, 40]

dessin = False
reseau = False
menu = True

while (True):

	while (menu):

		bouton_quit(posquit, textquit, shades, screenmain)
		bouton(posreseau, textreseau, shades, screenmain)
		bouton(posdessin, textdessin, shades, screenmain)

    	# stores the (x,y) coordinates into
		# the variable as a tuple
		mouse = pygame.mouse.get_pos()

		for ev in pygame.event.get():

			if ev.type == pygame.QUIT:
				pygame.quit()

			# checks if a mouse is clicked
			if ev.type == pygame.MOUSEBUTTONDOWN:

				# if the mouse is clicked on the
				# button the game is terminated
				if posquit[0] <= mouse[0] <= posquit[0]+posquit[2] and posquit[1] <= mouse[1] <= posquit[1]+posquit[3]:
					pygame.quit()
				elif posdessin[0] <= mouse[0] <= posdessin[0]+posdessin[2] and posdessin[1] <= mouse[1] <= posdessin[1]+posdessin[3]:
					dessin = True
					menu = False
					screenmain.fill((255, 255, 255))

				elif posreseau[0] <= mouse[0] <= posreseau[0]+posreseau[2] and posreseau[1] <= mouse[1] <= posreseau[1]+posreseau[3]:
					reseau = True
					menu = False
					screenmain.fill((255, 255, 255))

    	# updates the frames of the game
		pygame.display.update()

	while dessin:
		bouton(posfichier, textfichier, shades, screenmain)
		bouton(posretour,textretour,shades,screenmain)
		bouton(postest,texttest,shades,screenmain)
		mouse = pygame.mouse.get_pos()
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				pygame.quit()
			if ev.type == pygame.MOUSEBUTTONDOWN:
			
				if posretour[0] <= mouse[0] <= posretour[0]+posretour[2] and posretour[1] <= mouse[1] <= posretour[1]+posretour[3]:
						menu=True
						dessin=False
				elif posfichier[0] <= mouse[0] <= posfichier[0]+posfichier[2] and posfichier[1] <= mouse[1] <= posfichier[1]+posfichier[3]:
					subprocess.call(['mspaint', 'image.png'])
				elif postest[0] <= mouse[0] <= postest[0]+postest[2] and postest[1] <= mouse[1] <= postest[1]+postest[3]:
					paint.run()
				
		

		pygame.display.update()

	while reseau:
     
		type=""
		nblayers=0
		nbneuronnes=0
  
		bouton(posretour, textretour, shades, screenmain)
		bouton(poscreer,textcreer,shades,screenmain)
		bouton(poschoisir,textchoisir,shades,screenmain)
		mouse = pygame.mouse.get_pos()
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				pygame.quit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
				if posretour[0] <= mouse[0] <= posretour[0]+posretour[2] and posretour[1] <= mouse[1] <= posretour[1]+posretour[3]:
						menu=True
						dessin=False
				elif poschoisir[0] <= mouse[0] <= poschoisir[0]+poschoisir[2] and poschoisir[1] <= mouse[1] <= poschoisir[1]+poschoisir[3]:
					type,nblayers,nbneuronnes=choixreseau.getinfo()
				elif poscreer[0] <= mouse[0] <= poscreer[0]+poscreer[2] and poscreer[1] <= mouse[1] <= poscreer[1]+poscreer[3]:
					test.run(type,nblayers,nbneuronnes)

		pygame.display.update()
