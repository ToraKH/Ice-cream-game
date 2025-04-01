from data.object import Object
import pygame as pg
import random
import data.config as cng

class Scoop(Object):
    """represents an ice cream scoop"""
    def __init__(self, pos_x, pos_y, image, flavor, id):
        super().__init__(image)
        self.position = pg.math.Vector2(pos_x, pos_y) 
        self.rect = pg.rect.Rect(self.position.x, self.position.y, self.width, self.height)
        self.speed_y = random.uniform(0.3, 1)
        self.flavor = flavor
        self.caught = False
        self.number = -1
        self.customer_id = id


    def update(self):
        """make obstacle fall down from top of screen"""
        if self.caught == False:
            self.position.y += self.speed_y 
            self.rect.y = self.position.y 
        if self.position.y >= cng.FLOOR:
            self.kill()
          

