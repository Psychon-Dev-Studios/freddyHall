""" Office-related modules """

from modules.constants import *
from modules.office.camera import PATH
import pygame
from pygame import *


class office_image(pygame.sprite.Sprite):
    def __init__(self):
        super(office_image, self).__init__()
        self.surf = pygame.image.load(PATH + "/assets/office_background.png").convert() # Load the office image
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2)) # Position


    def update(VOID, screen, power):
        """ Update the object """
        power = int(power)
        if (power != 0) and not power < 0: # Only show the real image if there is power
            surf = pygame.image.load(PATH + "/assets/office_background.png").convert()
        
        else: # Show the blackout screen instead
            surf = pygame.image.load(PATH + "/assets/office_background_outage.png")
        surf.set_colorkey((0,0,0), RLEACCEL)
        rect = surf.get_rect()

        screen.blit(surf, rect)