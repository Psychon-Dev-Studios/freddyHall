""" Camera go up, camera go down. Camera go up, camera go down. Bonnie go boo, I go blue.\n
Camera panel-related functions"""

import sys, os
import pygame
from pygame import *

from modules.constants import *
PATH = sys.path[0]

class camera_panel(pygame.sprite.Sprite): # Camera class
    def __init__(self): # Create the entitiy
        super(camera_panel, self).__init__() # Read the documentation for super if you're interested
        self.surf = pygame.image.load(PATH + "/assets/camera/empty_frame.png").convert() # Load the empty frame
        self.surf.set_colorkey((0,0,0), RLEACCEL) # See previous iterations of the code
        self.rect = self.surf.get_rect()
        self.rect.center=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(VOID, ID, screen, camera_active):
        """ Update the object """
        try:
            surf = pygame.image.load(PATH + "/assets/camera/%s.png"%ID).convert() # Load the correct camera
        except Exception as err:
            surf = pygame.image.load(PATH + "/assets/camera/camera_down.png").convert() # Camera not found, load missing!
        surf.set_colorkey((0,0,0), RLEACCEL)
        rect = surf.get_rect()

        if camera_active == True: # Only run the code below if the camera is open
            screen.blit(surf, rect)

    def open(cameraID, screen, displayGroup, entity, clock):
        """ Handles the opening of the camera and the loading of the UI """
        camera_panel.showStaticAnimation(screen, clock) # Show static for a second
        try:
            entity.surf = pygame.image.load(PATH + "/assets/camera/%s.png"%cameraID).convert() # Load the camera
        except:
            entity.surf = pygame.image.load(PATH + "/assets/camera/camera_down.png").convert() # Load missing image
        entity.surf.set_colorkey((0,0,0), RLEACCEL)
        entity.rect = entity.surf.get_rect()
        entity.rect.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)

        displayGroup.add(entity)

    def close(displayGroup, display):
        """ Handles the closing of the camera and the deloading of the UI """

        for object in displayGroup: # Unloads everything in the camera UI. This includes the minimap, hence why camera_mmap does not include deload()
            object.kill() # Unload the assets
        
        camera_panel.update(None, "empty_frame", display, False) # Hide everythin

    def showStaticAnimation(screen, clock):
        floop = 0 # Times the animation has looped
        while floop < 1:
            for frame in os.listdir(PATH + "/assets/camera/staticFrames"):
                try:
                    surf = pygame.image.load(PATH + "/assets/camera/staticFrames/%s"%frame).convert_alpha() # Show the next frame in the animation
                    surf.set_colorkey((0,0,0), RLEACCEL)
                    rect = surf.get_rect()
                    screen.blit(surf, rect)

                    pygame.display.update(rect) # Update
                    clock.tick(30)
                    clock.get_fps() # Update FPS
                except:NotImplemented # ignore the stupid .ini file GDrive makes
                
            floop += 1 # Increase frames looped

    # def animatronicMovementDetected(screen, clock):
        
    #     floop = 0
    #     while floop < 3:
    #         for frame in os.listdir(PATH + "/assets/camera/moveDistortEffectFrames"):
    #             try:
    #                 screen.fill((0,0,0))
    #                 surf = pygame.image.load(PATH + "/assets/camera/moveDistortEffectFrames/%s"%frame).convert_alpha()
    #                 surf.set_colorkey((0,0,0), RLEACCEL)
    #                 rect = surf.get_rect()
    #                 screen.blit(surf, rect)

    #                 pygame.display.update(rect)
    #                 clock.tick(60)
    #                 clock.get_fps()
    #             except:NotImplemented # ignore the stupid .ini file GDrive makes
                
    #         floop += 1

    def animatronicMovementDetected(screen, clock, camera): # Movement detected, glitch the camera
        try:
            screen.fill((0,0,0))

            pygame.display.update()

            floop = 0 # Frames looped
            ttloop = 5 # Times To Loop

            DPATH = PATH + "/assets/camera/distort"

            """ ALL ITERATIONS OF THE CODE BELOW ARE THE SAME, ONLY DIFFERENT IN THAT THEY CHANGE WHICH CAMERA GLITCHES """
            if camera == 1: # Check which camera is active
                while floop != ttloop: 
                    for frame in os.listdir(DPATH + "/1"): # Load the frames
                        try:
                            screen.fill((0,0,0)) # Fill screen with black
                            surf = pygame.image.load(DPATH + "/1/%s"%frame).convert_alpha() # Load glitch frame
                            surf.set_colorkey((0,0,0), RLEACCEL)
                            rect = surf.get_rect()
                            screen.blit(surf, rect) # Draw    
                            pygame.display.update(rect) # Update the screen
                            clock.tick(60) # Limit frame rate
                            clock.get_fps()
                            
                        except:NotImplemented # ignore the stupid .ini file GDrive makes

                    floop += 1

            elif camera == 2:
                while floop != ttloop:
                    for frame in os.listdir(DPATH + "/2"):
                        try:
                            screen.fill((0,0,0))
                            surf = pygame.image.load(DPATH + "/2/%s"%frame).convert_alpha()
                            surf.set_colorkey((0,0,0), RLEACCEL)
                            rect = surf.get_rect()
                            screen.blit(surf, rect)    
                            pygame.display.update(rect)
                            clock.tick(60)
                            clock.get_fps()
                            
                        except:NotImplemented # ignore the stupid .ini file GDrive makes

                    floop += 1
            elif camera == 3:
                while floop != ttloop:
                        for frame in os.listdir(DPATH + "/3"):
                            try:
                                screen.fill((0,0,0))
                                surf = pygame.image.load(DPATH + "/3/%s"%frame).convert_alpha()
                                surf.set_colorkey((0,0,0), RLEACCEL)
                                rect = surf.get_rect()
                                screen.blit(surf, rect)    
                                pygame.display.update(rect)
                                clock.tick(60)
                                clock.get_fps()
                                
                            except:NotImplemented # ignore the stupid .ini file GDrive makes

                        floop += 1

            elif camera == 4:
                while floop != ttloop:
                        for frame in os.listdir(DPATH + "/4"):
                            try:
                                screen.fill((0,0,0))
                                surf = pygame.image.load(DPATH + "/4/%s"%frame).convert_alpha()
                                surf.set_colorkey((0,0,0), RLEACCEL)
                                rect = surf.get_rect()
                                screen.blit(surf, rect)    
                                pygame.display.update(rect)
                                clock.tick(60)
                                clock.get_fps()
                                
                            except:NotImplemented # ignore the stupid .ini file GDrive makes

                        floop += 1
            elif camera == 5:
                while floop != ttloop:
                        for frame in os.listdir(DPATH + "/5"):
                            try:
                                screen.fill((0,0,0))
                                surf = pygame.image.load(DPATH + "/5/%s"%frame).convert_alpha()
                                surf.set_colorkey((0,0,0), RLEACCEL)
                                rect = surf.get_rect()
                                screen.blit(surf, rect)    
                                pygame.display.update(rect)
                                clock.tick(60)
                                clock.get_fps()
                                
                            except:NotImplemented # ignore the stupid .ini file GDrive makes

                        floop += 1

            elif camera == 6:
                while floop != ttloop:
                        for frame in os.listdir(DPATH + "/6"):
                            try:
                                screen.fill((0,0,0))
                                surf = pygame.image.load(DPATH + "/6/%s"%frame).convert_alpha()
                                surf.set_colorkey((0,0,0), RLEACCEL)
                                rect = surf.get_rect()
                                screen.blit(surf, rect)    
                                pygame.display.update(rect)
                                clock.tick(60)
                                clock.get_fps()
                                
                            except:NotImplemented # ignore the stupid .ini file GDrive makes

                        floop += 1

        except:NotImplemented # ignore the stupid .ini file GDrive makes



class camera_mmap(pygame.sprite.Sprite): # Minimap class
    widthOffset, heightOffset = 200, 155 # Where to position it

    def __init__(self): # Initialize
        super(camera_mmap, self).__init__()
        self.surf = pygame.image.load(PATH + "/assets/camera/minimap.png").convert_alpha()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center=((SCREEN_WIDTH - camera_mmap.widthOffset, SCREEN_HEIGHT-camera_mmap.heightOffset))

    def load(entity, displayGroup):
        entity.surf = pygame.image.load(PATH + "/assets/camera/minimap.png").convert_alpha()
        entity.surf.set_colorkey((0,0,0), RLEACCEL)
        entity.rect = entity.surf.get_rect()
        entity.rect.center=((SCREEN_WIDTH - camera_mmap.widthOffset, SCREEN_HEIGHT-camera_mmap.heightOffset))

        displayGroup.add(entity)

    def update(VOID, VOID2, screen, VOID3):
        surf = pygame.image.load(PATH + "/assets/camera/minimap.png").convert_alpha()
        surf.set_colorkey((0,0,0), RLEACCEL)
        rect = surf.get_rect()
        rect.center=((SCREEN_WIDTH - camera_mmap.widthOffset, SCREEN_HEIGHT-camera_mmap.heightOffset))

        screen.blit(surf, rect)