import pygame as pg
import data.config as cng
from data.player import Player
from data.scoop import Scoop
import data.interface as interface
import data.animater as animater
from data.customer import Customer
from data.trash import TrashCan
import random



class Manager():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((cng.SCREEN_X, cng.SCREEN_Y))
        self.clock = pg.time.Clock()
        # self.fruit_number = 0
        self.spawn_timer = 3000
        self.current_image_index = 0
        self.max_orders = 5
        self.num_orders = 0
        self.game = "starting"
        self.last_spawn = pg.time.get_ticks()

        self.load_images()
        index = random.randint(0,4)
        self.game_bg = self.bg_img[index]
        self.sprite_init()

        x = (cng.CUSTOMERAREA-cng.MARGIN_X)/2
        # y = (cng.SCREEN_Y)/5
        pos1 = (x, 1*100+1*54)
        pos2 = (x, 2*100+2*54)
        pos3 = (x, 3*100+3*54)
        # pos4 = (x, 500)
        # pos5 = (x, 600)
        self.make_customer(pos1, 1)
        self.make_customer(pos2, 2)
        self.make_customer(pos3, 3)
        # self.make_customer(pos4, 4)
        # self.make_customer(pos5, 5)


        
        pg.mouse.set_visible(False)
        #interface.play_music() 
        self.loop()

        
        
        
    

    def load_images(self):
        """Loads and scales the images"""
        self.scoop_images = [
            (pg.image.load(cng.IMG1).convert_alpha(),cng.FLAVOR1),
            (pg.image.load(cng.IMG2).convert_alpha(),cng.FLAVOR2),
            (pg.image.load(cng.IMG3).convert_alpha(),cng.FLAVOR3),
            (pg.image.load(cng.IMG4).convert_alpha(),cng.FLAVOR4),
            (pg.image.load(cng.IMG5).convert_alpha(),cng.FLAVOR5),
            (pg.image.load(cng.IMG6).convert_alpha(), cng.FLAVOR6)
        ]
        self.scoop_images = [(pg.transform.scale(img, (img.get_width()*2, img.get_height()*2)), flavor) for img, flavor in self.scoop_images]


        self.player_img1 = pg.image.load(cng.CONE_IMG).convert_alpha() 
        self.player_img1 = pg.transform.scale(self.player_img1,(self.player_img1.get_width()*3, self.player_img1.get_height()*3))

        # Load backgrounds
        self.start_bg = pg.image.load(cng.START)
        self.start_bg = pg.transform.scale(self.start_bg,(cng.SCREEN_X, cng.SCREEN_Y)) 
        self.start_bg.convert()
        self.end_bg = pg.image.load(cng.END)
        self.end_bg = pg.transform.scale(self.start_bg,(cng.SCREEN_X, cng.SCREEN_Y)) 
        self.end_bg.convert()
        self.credit_bg = pg.image.load(cng.CREDIT)
        self.credit_bg = pg.transform.scale(self.credit_bg,(cng.SCREEN_X, cng.SCREEN_Y)) 
        self.credit_bg.convert()


        # Load game backgrounds
        self.bg_img = [
            pg.image.load(cng.BG1).convert_alpha(),
            pg.image.load(cng.BG2).convert_alpha(),
            pg.image.load(cng.BG3).convert_alpha(),
            pg.image.load(cng.BG4).convert_alpha(),
            pg.image.load(cng.BG5).convert_alpha()
        ]

        # Scale and convert images
        self.bg_img = [pg.transform.scale(img, (cng.SCREEN_X, cng.SCREEN_Y)) for img in self.bg_img]
        self.bg_img = [img.convert() for img in self.bg_img]


    def sprite_init(self):
        """Initializes sprite objects"""
        self.player_group = pg.sprite.Group()
        self.player = Player(self.player_img1)
        self.player_group.add(self.player)
        # Initialize fruit groups
        self.scoop_groups = [pg.sprite.Group() for _ in range(len(self.scoop_images))]
        self.ice_cream_group = pg.sprite.Group()

        self.customer_scoop_group = pg.sprite.Group()

        self.trash_group = pg.sprite.Group()
        self.trash = TrashCan(self.screen)
        self.trash_group.add(self.trash)

        self.customer_group = pg.sprite.Group()


        
    def spawn_scoop(self):
        """Spawns the scoop on the screen"""        
        for i, (image, flavor) in enumerate(self.scoop_images):
            for _ in range(random.randint(0, 2)):  # adjust the range to control the number of fruits spawned
                x = random.randint(cng.CUSTOMERAREA, cng.SCREEN_X - image.get_width())
                y = 0
                scoop = Scoop(x, y, image, flavor, -1)
                self.scoop_groups[i].add(scoop)

    def make_customer_order(self, scoop_img, pos, id):
        """ create a new customer with a new, random order """
        customer = Customer(self.player_img1, pos, id)
        self.customer_group.add(customer)
        customer.create_order(scoop_img, self.customer_scoop_group)

    def make_customer(self, pos, id):
        print(f"POSITION: {pos}")
        # pos_x = 30*num_orders#(cng.CUSTOMERAREA-self.player_img1.get_width())/2
        # pos_y = 400#cng.SCREEN_Y-(num_orders)*(self.player_img1.get_height()+ 5*pg.image.load(cng.IMG1).get_height()) - cng.MARGIN_Y
        # pos = (pos_x, pos_y)
        self.make_customer_order(self.scoop_images, pos, id)

    def loop(self):
        """Main loop for manager. Checks the event for exit strategy, and
           updates all the objects""" 
        while True:
            # Process events
            for event in pg.event.get():
                    
                if event.type == pg.QUIT:
                    self.game = "credits"

                
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.game = "credits"
                    

            #--------------START-SCREEN--------------------------
                # Startscreen
            if self.game == "starting":
                #Draw starting screen
                status = interface.start_screen(self.screen, self.start_bg)
                if status:
                    self.game = "on"

                
               
            #--------------GAME-SCREEN---------------------------
                    
            #Let the games begin...
            if self.game == "on":

                self.screen.blit(self.game_bg, (0,0))  
                self.event()
                #Updates sprites
                self.update()
                #Maintains 60 frames per second
                self.clock.tick(60)


            
            if self.game == "credits":
                interface.show_credit(self.screen, self.credit_bg)


    def event(self):
        """pg event"""
        
        current_time = pg.time.get_ticks()
        if current_time - self.last_spawn >= self.spawn_timer:
            self.spawn_scoop()
            self.last_spawn = current_time
        self.clock.tick(60)  # Frames per second


    def update(self):
        """Updates all objects through sprite's group update"""

        # draw rectangler behind customers and the floor
        pg.draw.rect(self.screen, (225,128,128),pg.Rect(0, 0, cng.CUSTOMERAREA, cng.SCREEN_Y))
        pg.draw.rect(self.screen, (128,128,128),pg.Rect(0, cng.FLOOR+25, cng.SCREEN_X, cng.SCREEN_Y))

        self.player_group.draw(self.screen)
        self.player.update()

        self.trash_group.draw(self.screen)

        for scoop_group in self.scoop_groups:
            scoop_group.update()
            scoop_group.draw(self.screen)
    
       
      
        for customer in self.customer_group:
            # print(f"CUSTOMER ID: {id(customer)}, X: {customer.rect.x}, Y: {customer.rect.y}")

            customer.update()        
            for customer_scoop in self.customer_scoop_group:
                if customer.id == customer_scoop.customer_id:
                    customer.move_scoop(customer_scoop)
            

        self.customer_scoop_group.draw(self.screen)
        self.customer_group.draw(self.screen)

        
        
        
        for player in self.player_group:

            #Check if player has caught scoop
            for scoop_group in self.scoop_groups:
                collected_scoops = pg.sprite.spritecollide(player, scoop_group, False)
                for scoop in collected_scoops:
                    if not scoop.caught:
                        scoop.caught = True
                        player.add_to_cone(scoop)
                        scoop.remove(self.ice_cream_group)
                        self.ice_cream_group.add(scoop)
            
            # check if player has delivered order
            customer_served_group = pg.sprite.spritecollide(player, self.customer_group, False)
            for customer in customer_served_group:
                if customer.validate_order(self.player.scoops) == 0:
                    print(f"ORDER IS CORRECT")
                    
                    id = -1
                    scoopnr = 0
                    for scoop in self.customer_scoop_group: # remove the customer scoops
                        if scoop.customer_id == customer.id:
                            id = customer.id
                            print(f"CUSTOMER ID {customer.id}")
                            scoop.kill()
                            customer.remove_order() 

                            # remove player scoops
                            self.player.scoops = {}
                            for scoop in self.ice_cream_group:
                                scoopnr += 1
                                scoop.kill()
                            
                            
                            
                    # create new customer
                    if id != -1:
                        print(f"NEW CUSTOMER ID {id}")
                        x = (cng.CUSTOMERAREA-cng.MARGIN_X)/2
                        self.make_customer((x,id*100+id*54), id)        
                        # self.make_customer((x,id*180), id)
                        # else:
                        #     print("Not correct id")
                    
                    self.player.score += 5*scoopnr

                # # loose points for delivering wrond ice cream
                # elif customer.validate_order(self.player.scoops) == 2:
                #     self.player.score -= 10
                     

            #throw away scoops if going in trashcan
            going_in_trash_list = pg.sprite.spritecollide(self.trash, self.ice_cream_group, False)
            if len(going_in_trash_list) > 0:
                self.player.scoops = {}
                for scoop in self.ice_cream_group:
                    scoop.kill()

          

        for scoop in self.ice_cream_group:
            player.move_scoop(scoop)
            

        interface.show_text(self.screen, self.player)
        pg.display.update()


if __name__ == "__main__":
    Manager()