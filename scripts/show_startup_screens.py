"""Startup screen. Includes the logo, controls, and disclaimer."""

import pygame, time as systime, os, sys
from modules.verifier import file_checksum
from modules.constants import manifest
from pygame import *
from modules.fakes import *

PATH = sys.path[0]

from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader 
spec = spec_from_loader("controllers", SourceFileLoader("controllers", PATH + "/settings/controller.conf"));sets = module_from_spec(spec);spec.loader.exec_module(sets)
sys.modules['controller_keys'] = sets # Load the config file as a python module, letting us use the settings inside as variables

from controller_keys import *

def startup_screens(screen, SCREEN_WIDTH, SCREEN_HEIGHT, PATH):
    if pygame.joystick.get_count() != 0:
        controller = pygame.joystick.Joystick(JOY_ID)
        connected = True
    else:
        class controller:
            def get_axis(void):return 0
            def get_button(void):return 0
        connected = False
    
    # Show the title screen
    title_surf = pygame.image.load(PATH + "/assets/title_screen.png").convert() # Loads the image
    title_surf.set_colorkey((255,255,255), RLEACCEL) # Set the image's background to black to make it ~vanish~
    title_rect = title_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
    screen.blit(title_surf, title_rect) # Prepare the image to be shown on-screen

    pygame.display.flip() # Update the screen, showing the image

    systime.sleep(1.23)

    if (connected): # Warn the user about potential instabilities with Gamepad support (Pygame really really hates controllers!)
        screen.fill((0, 0, 0))
        control_surf = pygame.image.load(PATH + "/assets/gp_controls/gamepad_unstable.png").convert() # Loads the image
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
                if (event.type == KEYDOWN) and (event.key == K_RETURN):waiting = False
                elif (event.type == JOYBUTTONDOWN and controller.get_button(A_ID)):waiting = False
            polling_rate.tick(30)


    if (open(PATH + "/settings/checksum.option", "r").read() == "true") or manifest.isSuperSecretBuild == True:
        # file_checksum(screen)
        ## !! Hotfix 2 resolved !! removed because of dramatically increased load times
        NotImplemented

    if (manifest.autoUpdateSupported == False) and (manifest.isSuperSecretBuild == False):
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
                if (event.type == KEYDOWN) and (event.key == K_RETURN):waiting = False
                elif (event.type == JOYBUTTONDOWN and controller.get_button(A_ID)):waiting = False
            polling_rate.tick(30)

    if (manifest.isSuperSecretBuild == True):
        screen.fill((0, 0, 0))
        control_surf = pygame.image.load(PATH + "/assets/secret-build.png").convert() # Loads the image
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
                if (event.type == KEYDOWN) and (event.key == K_RETURN):waiting = False
                elif (event.type == JOYBUTTONDOWN and controller.get_button(A_ID)):waiting = False
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
                if (event.type == KEYDOWN) and (event.key == K_RETURN):waiting = False
                elif (event.type == JOYBUTTONDOWN and controller.get_button(A_ID)):waiting = False

            polling_rate.tick(30)
    

    screen.fill((0, 0, 0))

    if open(PATH + "/settings/showControls.option", "r").read() == "true":
        if not (connected):control_surf = pygame.image.load(PATH + "/assets/how_to_play.png").convert() # Loads the image
        else:
            if (JOY_CFG == "ASUS_GP"):control_surf = pygame.image.load(PATH + "/assets/gp_controls/asus_gp.png").convert() # Loads the image
            elif (JOY_CFG == "X360"):control_surf = pygame.image.load(PATH + "/assets/gp_controls/x360.png").convert() # Loads the image
            elif (JOY_CFG == "PS4"):control_surf = pygame.image.load(PATH + "/assets/gp_controls/ps4.png").convert() # Loads the image
            elif (JOY_CFG == "MS_SIDEWINDER"):control_surf = pygame.image.load(PATH + "/assets/gp_controls/ms_sw.png").convert() # Loads the image
            else:control_surf = pygame.image.load(PATH + "/assets/gp_controls/unknown.png").convert() # Loads the image
        control_surf.set_colorkey((0,0,0), RLEACCEL) # Set the image's background to black to make it ~vanish~
        control_rect = control_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(control_surf, control_rect) # Prepare the image to be shown on-screen

        pygame.display.flip()

        waiting = True # Make the loop below run

        while waiting:
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if (event.type == KEYDOWN) and (event.key == K_RETURN):waiting = False
                elif (event.type == JOYBUTTONDOWN and controller.get_button(A_ID)):waiting = False

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
            if (event.type == KEYDOWN) and (event.key == K_RETURN):waiting = False
            elif (event.type == JOYBUTTONDOWN and controller.get_button(A_ID)):waiting = False

            polling_rate.tick(30)