import pygame as pg
import data.config as cng

class TrashCan(pg.sprite.Sprite):  # Ensure TrashCan inherits from Sprite
    def __init__(self, screen):
        super().__init__()  # Call the base class constructor to initialize the sprite
        
        # Define position and size of the trash can
        self.image = pg.Surface((20, 20))  # Create a surface for the trash can (20x20 size)
        self.image.fill((0, 0, 0))  # Fill the surface with black color (you can change the color)
        
        self.rect = self.image.get_rect()  # Get the rect of the image
        self.rect.topleft = ((cng.SCREEN_X-20)/2, cng.SCREEN_Y-60)  # Set the position (top-left corner)
        
    def update(self):
        # Add any updates to position, animation, or behavior for the trash can here
        pass