from data.icecreamcone import IceCreamCone
import pygame as pg
import random 
import data.config as cng
import math

class Player(IceCreamCone):
    def __init__(self, image):
        super().__init__(image)
        self.position = pg.math.Vector2(random.randint(0+self.image.get_width(),cng.SCREEN_X-self.image.get_width()), cng.FLOOR-self.image.get_height())
        self.rect = pg.rect.Rect(self.position.x, self.position.y, self.width, self.height)
        self.num_cones = 0
        self.scoops = {}
        self.score = 0


    def move_up(self):
        self.position.y -= cng.SPEED_X
    
    def move_down(self):
        self.position.y += cng.SPEED_X

    def move_right(self):
        self.position.x += cng.SPEED_X 

    def move_left(self):
        self.position.x -= cng.SPEED_X 

    def add_to_cone(self, scoop):
        """Gjør det som skjer når man får en scoop"""
        # print("Hekki sir")
        # self.num_cones += 1
        # scoop.number = self.num_cones -1
        scoop.number = len(self.scoops)
        self.scoops[scoop.number] = scoop.flavor

        # scoop.got_caught(height_vector)
        # self.scoops[self.num_cones] = scoop.flavor
        #feks adder rect til rect
        #adder kule til hvilke kuler det er
        #dict med key som kulenr og smak som "" value??
        

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
        
        #Update rectangle
        self.rect.topleft = self.position

        self.handle_input()
        if self.position.x < 0 - self.image.get_width():  
            self.position.x = cng.SCREEN_X  
        elif self.position.x > cng.SCREEN_X:  
            self.position.x = 0 - self.image.get_width()
   
    def handle_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.move_left()
        if keys[pg.K_d]:
            self.move_right()
        if keys[pg.K_w] and self.position.y > 0:
            self.move_up()
        if keys[pg.K_s] and self.position.y < cng.SCREEN_Y - self.image.get_height():
            self.move_down()

