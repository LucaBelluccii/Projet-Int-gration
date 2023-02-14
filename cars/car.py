import pygame as pg
import math

STEERING_ANGLE = 5
ACCELERATION = 0.7
DECCELERATION = 3
MAX_VELOCITY = 12

class Car:
    def __init__(self,x,y,width,height,imgPath):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.angle = 90

        

        self.image = pg.image.load(imgPath).convert_alpha()
        self.image = pg.transform.scale(self.image,(height,width))
        self.rect = pg.Rect(x, y, height, width)
        self.surface = pg.Surface((height, width),pg.SRCALPHA,32) 
        self.surface.blit(self.image, (0, 0))

        
        
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

        
        
        

        self.clamp()

        self.x -= self.vel * math.cos(math.radians(self.angle))
        self.y -= self.vel * math.sin(math.radians(self.angle))
        self.rect.topleft = (self.x,self.y)

        self.inputs = [False,False,False,False]
    

    def clamp(self):
        if self.vel<0:
            self.vel = 0
        elif self.vel>MAX_VELOCITY:
            self.vel = MAX_VELOCITY

    def draw(self,window):
        self.rect.topleft = (int(self.x), int(self.y))
        rotated = pg.transform.rotate(self.surface, -self.angle+180)
        surface_rect = self.surface.get_rect(topleft = self.rect.topleft)
        new_rect = rotated.get_rect(center = surface_rect.center)
        window.blit(rotated, new_rect.topleft)
