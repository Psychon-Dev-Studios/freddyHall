""" DJMM module container """

import pygame
from pygame import *
import sys, os
PATH = sys.path[0]
from modules.constants import *

clock = pygame.time.Clock()

def jumpscare(screen, SCREEN_WIDTH, SCREEN_HEIGHT): # Play the jumpscare
    """Show DJMM's jumpscare"""
    
    frameLooped = 0 # How many frames are looped

    pygame.mixer.Channel(1).play(pygame.mixer.Sound(PATH + '/assets/audio/djmm_jumpscare.wav')) # Play jumpscare sound
    while frameLooped < 55: # Loop the frames 55 times
        for frame in os.listdir(PATH + "/assets/djmm/frames"):
            screen.fill((0,0,0)) # Fill with black

            if (".gif" in frame or ".png" in frame): # Only load the safe files, not .ini
                surf = pygame.image.load(PATH + "/assets/djmm/frames/%s"%frame).convert() # Loads the image
                surf.set_colorkey((0,0,0), RLEACCEL) # Configures the image to be processed at full RGB spectrum at low quality (for speed)
                rect = surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
                screen.blit(surf, rect) # Prepare the image to be shown on-screen
                pygame.event.get()

                pygame.display.flip() # Update
                frameLooped += 1 # Update frames looped
                clock.tick(40)

    return "Jumpscare"


class djmm(pygame.sprite.Sprite):
    def __init__(self): # Initialize DJMM
        super(djmm, self).__init__()
        self.surf = pygame.image.load(PATH + "/assets/djmm/dj.jpeg").convert() # Load the image
        self.surf.set_colorkey((255,255,255), RLEACCEL) # Try to blank out the background so it's transparent
        self.rect = self.surf.get_rect()
        self.rect.center=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2)) # Position

    def update(VOID, mode, screen, active_camera, location_f, location_mm): # Update DJMM
        """ Mode can be: 'normal' (update display) or 'destroy' (get that weird... thing? outta here!) """

        if (mode == "normal") and (str(active_camera) == str(location_mm)): # Render the image
            surf = pygame.image.load(PATH + "/assets/djmm/dj.jpeg").convert() # Load sprite
            surf.set_colorkey((255,255,255), RLEACCEL) # Blank out the background
            rect = surf.get_rect()
            rect.center = (((SCREEN_WIDTH/2)+200, SCREEN_HEIGHT/2)) # Position

            screen.blit(surf, rect) # Render

        else:
            NotImplemented
            # This makes the entity dissapear, since it no longer renders itself