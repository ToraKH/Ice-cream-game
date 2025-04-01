from data.object import Object
import pygame as pg
import random 
import data.config as cng
import math

class IceCreamCone(Object):
    def __init__(self, image):
        super().__init__(image)
        self.position = pg.math.Vector2(random.randint(0+self.image.get_width(),cng.SCREEN_X-self.image.get_width()), cng.FLOOR-self.image.get_height())
        self.rect = pg.rect.Rect(self.position.x, self.position.y, self.width, self.height)
        self.num_cones = 0
        self.scoops = {}

    def move_up(self):
        pass
    
    def move_down(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def add_to_cone(self, scoop):
        """Gjør det som skjer når man får en scoop"""
        scoop.number = len(self.scoops)
        self.scoops[scoop.number] = scoop.flavor

    def move_scoop(self, scoop):
        scoop_height = scoop.image.get_height()
        overlap = 10
        y_offset = -scoop.number * (scoop_height - overlap)

        # Get correct stacking origin at top center of cone
        cone_top = self.rect.top +5
        cone_x = self.rect.centerx
        stack_origin = pg.math.Vector2(cone_x, cone_top)

        scoop.rect.midbottom = stack_origin + pg.math.Vector2(0, y_offset)



    def new_cone(self):
        """remove old flavors"""

    def update(self):
        pass
   
    def handle_input(self):
        pass

