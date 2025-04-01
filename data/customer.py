from data.icecreamcone import IceCreamCone
from data.scoop import Scoop
import pygame as pg
import random 
import data.config as cng



class Customer(IceCreamCone):
    def __init__(self, image, position, id):
        super().__init__(image)
        self.position = pg.math.Vector2(position) #pg.math.Vector2(random.randint(cng.CUSTOMERAREA-5*self.image.get_width()), cng.FLOOR-self.image.get_height())
        self.rect = pg.rect.Rect(self.position.x, self.position.y, self.width, self.height)
        self.num_cones = 0
        self.scoops = {}
        self.id = id

    
    def create_scoop(self, scoop_img, group):
        """ Creates a scoop on the screen at given coords """        
        # for i, (image, flavor) in enumerate(scoop_img):
        image, flavor = random.choice(scoop_img)
        x = 0
        y = 0
        id = self.id
        scoop = Scoop(x, y, image, flavor, id)
        scoop.caught = True #ensure the scoops wont fall down
        group.add(scoop)
        self.add_to_cone(scoop)
        print(f"Order: {flavor}")

    def create_order(self, scoop_img, group):
        """ generates a random order of max 5 random flavours """
        for _ in range(random.randint(1, 5)):  # adjust the range to control the number of scoops
            self.create_scoop(scoop_img, group)
        print("ORDER COMPLETE\n#########\n")
    
    def remove_order(self):
        """ remove order after finished """
        self.scoops = {}
        self.kill()

    def validate_order(self, order_scoops): # order_scoops is the players scoop dictionary
        """ check that the scoop order is correct """

        if len(self.scoops) != len(order_scoops): # check that there are correct number of scoops
            # print(f"wrong nr scoops: {self.scoops} vs registered {order_scoops}")

            # print("CUSTOMER")
            # for scoop in self.scoops:
            #     print(f"{scoop}")

            # print("PLAYER")
            # for scooper in order_scoops:
            #     print(f"{scooper}")
            return 1

        for i in range(len(self.scoops)): #check if order scoops = served scoops
            if self.scoops[i] != order_scoops[i]: 
                return 2

        # successfull!
        # self.remove_order() 
        return 0 
    



    
    

        
        
