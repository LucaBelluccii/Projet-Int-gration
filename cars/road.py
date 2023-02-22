import pygame as pg
class Road:
    def __init__(self,lanes,left,right):
        self.lanes = lanes
        self.left = left
        self.right = right
        
        self.rect = pg.Rect(left,float(-"inf"),right,float("inf"))