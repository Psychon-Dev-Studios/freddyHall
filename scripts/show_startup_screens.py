"""Startup screen. Includes the logo, controls, and disclaimer."""

import pygame, time as systime, os, sys
from modules.verifier import file_checksum
from modules.constants import manifest
from pygame import *

def startup_screens(screen, SCREEN_WIDTH, SCREEN_HEIGHT, PATH):
    
    # Show the title screen
    title_surf = pygame.image.load(PATH + "/assets/title_screen.png").convert() # Loads the image
    title_surf.set_colorkey((255,255,255), RLEACCEL) # Set the image's background to black to make it ~vanish~
    title_rect = title_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
    screen.blit(title_surf, title_rect) # Prepare the image to be shown on-screen

    pygame.display.flip() # Update the screen, showing the image

    systime.sleep(1.23)

    if (open(PATH + "/settings/checksum.option", "r").read() == "true"):
        file_checksum(screen)

    if (manifest.autoUpdateSupported == False):
        screen.fill((0, 0, 0))
        control_surf = pygame.image.load(PATH + "/assets/noAutoUpgrade.png").convert() # Loads the image
        control_surf.set_colorkey((0,0,0), RLEACCEL) # Set the image's background to black to make it ~vanish~
        control_rect = control_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(control_surf, control_rect) # Prepare the image to be shown on-screen
        pygame.display.flip()

        waiting = True # Make the loop below run
        # Create a new clock to configure key polling rate
        polling_rate = pygame.time.Clock()

        while waiting:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_RETURN:waiting = False
            polling_rate.tick(30)

    if (open(PATH + "/settings/disclaimer.option", "r").read() == "true"):
        screen.fill((0, 0, 0))
        control_surf = pygame.image.load(PATH + "/assets/disclaimer.png").convert() # Loads the image
        control_surf.set_colorkey((0,0,0), RLEACCEL) # Set the image's background to black to make it ~vanish~
        control_rect = control_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(control_surf, control_rect) # Prepare the image to be shown on-screen

        # mixer.music.load(PATH + "/assets/audio/fh_disclaimer_xep_trial_1.wav")
        # mixer.music.play()
        pygame.display.flip()

        waiting = True # Make the loop below run
        # Create a new clock to configure key polling rate
        polling_rate = pygame.time.Clock()

        while waiting:
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # If the Enter key is pressed, leave the controls screen
                    if event.key == K_RETURN:
                        waiting = False

            polling_rate.tick(30)
    

    screen.fill((0, 0, 0))

    if open(PATH + "/settings/showControls.option", "r").read() == "true":
        control_surf = pygame.image.load(PATH + "/assets/how_to_play.png").convert() # Loads the image
        control_surf.set_colorkey((0,0,0), RLEACCEL) # Set the image's background to black to make it ~vanish~
        control_rect = control_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(control_surf, control_rect) # Prepare the image to be shown on-screen

        pygame.display.flip()

        waiting = True # Make the loop below run

        while waiting:
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # If the Enter key is pressed, leave the controls screen
                    if event.key == K_RETURN:
                        waiting = False

            polling_rate.tick(30)


    if os.path.isfile(PATH + "/data/client") == True:
        screen.fill((0, 0, 0))

        control_surf = pygame.image.load(PATH + "/assets/mpx.png").convert() # Loads the image
        control_surf.set_colorkey((0,0,0), RLEACCEL) # Set the image's background to black to make it ~vanish~
        control_rect = control_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(control_surf, control_rect) # Prepare the image to be shown on-screen

        pygame.display.flip()

        waiting = True # Make the loop below run

        while waiting:
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # If the Enter key is pressed, leave the controls screen
                    if event.key == K_RETURN:
                        waiting = False

            polling_rate.tick(30)