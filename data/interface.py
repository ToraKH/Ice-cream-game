import pygame as pg
from pygame import mixer
import data.config as cng


# ============================================================= 
def start_screen(screen, start_bg):
    """ Shows the start screen"""
    screen.blit(start_bg, (0,0)) 
    
    key = pg.key.get_pressed()

    # Start game if pressed on start button
    if key[pg.K_SPACE]:
        pg.time.delay(150)
        return True   #start game

    #-----------------------------------------------------
    
    # Blit text
    font1 = pg.font.SysFont('arial', 21)
    font2 = pg.font.SysFont('arial', 70)
    title = font2.render('THE ICE CREAM COLLECTOR', True, (0,0,0))
    created_by = font1.render('A game by Tora K. Homme', True, (255,255,255))
    screen.blit(title, ((cng.SCREEN_X-title.get_width())/2, cng.SCREEN_Y/3+45))
    screen.blit(created_by, ((cng.SCREEN_X-created_by.get_width())/2, cng.SCREEN_Y-27))

    pg.display.update()    

# ============================================================= 


    



# ============================================================= 
def show_credit(screen, credit_bg):
    screen.blit(credit_bg, (0,0))
    font2 = pg.font.SysFont('arial', 50)
    font1 = pg.font.SysFont('arial', 21)
    
    #-----------------------------------------------------
    
    #Create text in the correct font
    credit_title = font2.render('CREDITS', True, (255, 255, 255))

    creators = font1.render('DEVELOPER & SUPPORT', True, (255, 255, 255))
    game_devs = font1.render('Game developer: Tora K. Homme', True, (255, 255, 255))
    em_sup = font1.render('Tester: Sigurd A. Lorentzen', True, (255, 255, 255))

    images = font1.render('IMAGES', True, (255, 255, 255))
    img = font1.render('Ice cream found at PIXILART' , True, (255, 255, 255))
    img2 = font1.render('Ice cream recolored by Tora K. Homme' , True, (255, 255, 255))
    img3 = font1.render('Backgrounds made by Tora K. Homme' , True, (255, 255, 255))

    # music = font1.render('MUSIC', True, (255, 255, 255))
    # song = font1.render('Song by Geoff Harvey', True, (255, 255, 255))

    #Print text at correct place of the screen
    screen.blit(credit_title, ((cng.SCREEN_X-credit_title.get_width())/2, 4*credit_title.get_height()))

    screen.blit(creators, ((cng.SCREEN_X-creators.get_width())/2, 12* creators.get_height()))
    screen.blit(game_devs, ((cng.SCREEN_X-game_devs.get_width())/2, 13*game_devs.get_height()))
    screen.blit(em_sup, ((cng.SCREEN_X-em_sup.get_width())/2, 14*em_sup.get_height()))

    screen.blit(images, ((cng.SCREEN_X-images.get_width())/2, 17*images.get_height()))
    screen.blit(img, ((cng.SCREEN_X-img.get_width())/2, 18*img.get_height()))
    screen.blit(img2, ((cng.SCREEN_X-img2.get_width())/2, 19*img2.get_height()))
    screen.blit(img3, ((cng.SCREEN_X-img3.get_width())/2, 20*img3.get_height()))
   

    pg.display.update() 
    pg.time.delay(4500)
    # Exit game if pressed
    exit()

def show_text(screen, player):
    """Prints text on screen"""
    # Register chosen font + its size
    font = pg.font.SysFont('arial', 20)
    score_player1 = font.render('Coins: ' + str(player.score), True, (255, 255, 255))
    screen.blit(score_player1, (15, cng.SCREEN_Y - 2*score_player1.get_height()))    

def play_music():
    """Plays the music"""
    #Initialise pygame music mixer
    mixer.init()
    #Load chosen music-file
    mixer.music.load((cng.MUSIC))
    #Adjust volume
    mixer.music.set_volume(cng.VOLUME)
    #Play music from the beginning
    mixer.music.play(-1, 0, 0)
    