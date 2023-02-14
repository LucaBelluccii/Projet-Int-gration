import pygame as pg
import math

STEERING_ANGLE = 1
ACCELERATION = 0.5
DECCELERATION = 1.5
MAX_VELOCITY = 5

class Car(pg.sprite.Sprite):
    def __init__(self,x,y,width,height,imgPath):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.angle = 90

        self.original_image = pg.image.load(imgPath).convert_alpha()
        self.original_image = pg.transform.scale(self.original_image,(height,width))

        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(topleft = (x,y))
        
        
        self.inputs = [False,False,False,False]#gas,brake,left,rigth

        self.vel = 0

    def update(self):
        
        #inputs
        

        if self.inputs[0]:
            self.vel+=ACCELERATION
        if self.inputs[1]:
            self.vel-=DECCELERATION
        if self.inputs[2]:
            self.angle -= STEERING_ANGLE
        if self.inputs[3]:
           self.angle +=STEERING_ANGLE

        
        self.image = self.rotate()
        

        self.clamp()

        self.x -= self.vel * math.cos(math.radians(self.angle))
        self.y -= self.vel * math.sin(math.radians(self.angle))
        self.rect.topleft = (self.x,self.y)

        self.inputs = [False,False,False,False]
    def rotate(self):
        self.image = pg.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)    

    def clamp(self):
        if self.vel<0:
            self.vel = 0
        elif self.vel>MAX_VELOCITY:
            self.vel = MAX_VELOCITY

    def draw(self,window):
        print(self.image)
        window.blit(self.image,self.rect)
