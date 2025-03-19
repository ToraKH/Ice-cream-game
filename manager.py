import pygame as pg
import data.config as cng
from data.player import Player
from data.scoop import Scoop
import data.interface as interface
import data.animater as animater
import random



class Manager():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((cng.SCREEN_X, cng.SCREEN_Y))
        self.clock = pg.time.Clock()
        # self.fruit_number = 0
        self.spawn_timer = 3000
        self.current_image_index = 0
        self.game = "starting"
        self.last_spawn = pg.time.get_ticks()
        self.load_images()
        index = random.randint(0,4)
        self.game_bg = self.bg_img[index]
        self.sprite_init()
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
        
    def spawn_scoop(self):
        """Spawns the scoop on the screen"""        
        for i, (image, flavor) in enumerate(self.scoop_images):
            for _ in range(random.randint(0, 2)):  # adjust the range to control the number of fruits spawned
                x = random.randint(cng.CUSTOMERAREA, cng.SCREEN_X - image.get_width())
                y = 0
                scoop = Scoop(x, y, image, flavor)
                self.scoop_groups[i].add(scoop)

    def add_scoop_to_cone(self, scoop):
        """adds the scoop to the cone"""
        


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
        self.player_group.draw(self.screen)
        self.player.update()
        
        for scoop_group in self.scoop_groups:
            scoop_group.update()
            scoop_group.draw(self.screen)
    
    

        #Check if player has caught fruit
        for player in self.player_group:
            for scoop_group in self.scoop_groups:
                collected_scoops = pg.sprite.spritecollide(player, scoop_group, False)
                for scoop in collected_scoops:
                    if not scoop.caught:
                        scoop.caught = True
                        player.add_to_cone(scoop)
                        scoop.remove(self.ice_cream_group)
                        self.ice_cream_group.add(scoop)
                    
        for scoop in self.ice_cream_group:
            player.move_scoop(scoop)
            

        
            

        interface.show_text(self.screen, self.player)
        pg.display.update()


if __name__ == "__main__":
    Manager()