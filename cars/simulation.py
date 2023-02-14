import pygame as pg
import car

pg.init()

WIDTH,HEIGHT = 400,600

FPS = 20

CLOCK = pg.time.Clock()

WINDOW = pg.display.set_mode((WIDTH,HEIGHT))

CAR_IMG_SRC = ".\\assets\\car.png"

car = car.Car(50,50,30,50,CAR_IMG_SRC)

WINDOW.fill((255,255,255))

running = True

while running:

    CLOCK.tick(FPS)

    WINDOW.fill((255,255,255))
    
    car.draw(WINDOW)
    car.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        car.inputs[0] = True
    if keys[pg.K_DOWN]:
        car.inputs[1] =True
    if keys[pg.K_LEFT]:
        car.inputs[2]=True
    if keys[pg.K_RIGHT]:
        car.inputs[3]=True
    
    for e in pg.event.get():
        if e.type==pg.QUIT:
            running = False


    pg.display.flip()