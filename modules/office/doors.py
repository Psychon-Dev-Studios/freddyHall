""" These doors should work in the opposite fashion...\n
Office door-related modules """

from modules.constants import *
import pygame, sys
from pygame import *

PATH = sys.path[0]

class door_left(pygame.sprite.Sprite):
    def __init__(self):
        super(door_left, self).__init__()
        self.surf = pygame.image.load(PATH + "/assets/office_door.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def close(screen):
        mixer.Channel(5).play(pygame.mixer.Sound(PATH + '/assets/audio/door_slam.wav')) # Play the door shut sound
        surf = pygame.image.load(PATH + "/assets/office_door.png").convert()
        surf.set_colorkey((255,255,255), RLEACCEL)
        rect = surf.get_rect()
        rect.center=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        pygame.mixer.Channel(6).play(pygame.mixer.Sound(PATH + "/assets/audio/door_slam.wav"))

        screen.blit(surf, rect)
        file = open(PATH + "/data/leftDoorStatus", "w")
        file.write("closed")
        file.close()

    def open():
        file = open(PATH + "/data/leftDoorStatus", "w")
        file.write("open")
        file.close()

    
    def update(VOID, screen, power):
        status = open(PATH + "/data/leftDoorStatus", "r").read() # Is the door open
        power = int(power)
        if (status == "closed") and power != 0 and not power < 0:
            surf = pygame.image.load(PATH + "/assets/office_door.png").convert()
            surf.set_colorkey((255,255,255), RLEACCEL)
            rect = surf.get_rect()
            rect.center=(((SCREEN_WIDTH/2)-289, SCREEN_HEIGHT/2))

            screen.blit(surf, rect)


class door_right(pygame.sprite.Sprite):
    def __init__(self):
        super(door_right, self).__init__()
        self.surf = pygame.image.load(PATH + "/assets/office_door.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center=(((SCREEN_WIDTH/2)-150, (SCREEN_HEIGHT/2)))

    def close(screen):
        surf = pygame.image.load(PATH + "/assets/office_door.png").convert()
        surf.set_colorkey((255,255,255), RLEACCEL)
        rect = surf.get_rect()
        rect.center=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        pygame.mixer.Channel(6).play(pygame.mixer.Sound(PATH + "/assets/audio/door_slam.wav"))

        screen.blit(surf, rect)

        file = open(PATH + "/data/rightDoorStatus", "w") # Write door status
        file.write("closed")
        file.close()

    def open():
        file = open(PATH + "/data/rightDoorStatus", "w") # Write door status
        file.write("open")
        file.close()

    def update(VOID, screen, power):
        status = open(PATH + "/data/rightDoorStatus", "r").read() # Read door status
        power = int(power) # Read power status
        if (status == "closed") and power != 0 and not power < 0: # Only run if there's enough power
            surf = pygame.image.load(PATH + "/assets/office_door.png").convert()
            surf.set_colorkey((255,255,255), RLEACCEL)
            rect = surf.get_rect()
            rect.center=(((SCREEN_WIDTH/2)+400, SCREEN_HEIGHT/2)) # Position the image

            screen.blit(surf, rect)