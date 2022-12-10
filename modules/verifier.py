"""Verifies various important information, such as if dependencies are available"""
import os, subprocess, tkinter, sys, time as systime, pygame
from modules.constants import manifest
from pygame import *
from tkinter import messagebox
from modules.constants import verified_checksum
PATH = sys.path[0]

def verify_dependencies():
    """Attempts to determine if any required modules are missing"""
    
    missing_dependencies = []

    try:
        import pygame
    except:
        missing_dependencies.append("pygame")

    try:
        import pygame_widgets
    except:
        missing_dependencies.append("pgw")

    try:import requests
    except:missing_dependencies.append("reqs")


    if (len(missing_dependencies) > 0):
        
        root = tkinter.Tk()
        root.iconify()
        installRequired = messagebox.askokcancel("Missing or Damaged Dependencies", "This program cannot be started because a required module is missing. Click OK to install the required modules, or Cancel to abort") # Show error
        root.destroy()

        if (installRequired == True):
            install_dependencies()
        else:
            os.abort()

def install_dependencies():
    """Attempt to install missing dependencies"""

    try:
        subprocess.call("pip install pygame") # Attempt to install pygame
        subprocess.call("pip install pygame_widgets")
        subprocess.call("pip install requests")
    except Exception as err:
        root = tkinter.Tk()
        root.iconify()
        keep_going = messagebox.askyesno("Install Failed", "Installation of a required module failed. Based on the following message, should we proceed anyways? Message: " + str(err)) # Show error
        root.destroy()

        if (keep_going == False):
            os.abort()

    try:
        import pygame, pygame_widgets, requests
        
    except Exception as err:
        root = tkinter.Tk()
        root.iconify()
        keep_going = messagebox.askyesno("Install Failed", "Initialization of a required module failed (likely due to a failed install). Based on the following message, should we proceed anyways? Message: " + str(err)) # Show error
        root.destroy()

        if (keep_going == False):
            os.abort()

def file_checksum(screen):
    if pygame.joystick.get_count() != 0:
        controller = pygame.joystick.Joystick(1)
    else:
        class controller:
            def get_axis(void):return 0
            def get_button(void):return 0
    checksum_dirs= ["/assets", "/settings"]

    full_checksum = []

    for targetDIR in checksum_dirs:
        generated_checksum = []
        index = 0

        for root, subfolders, filenames in os.walk(PATH + targetDIR):
            """ HOTFIX 2 """
            # generated_checksum.append(filenames)
            for file in filenames:
                """ HOTFIX 2 """
                if not ".pyc" in file:
                    generated_checksum.append(file)
                screen.fill((0,0,0))
                title_surf = pygame.image.load(PATH + "/assets/title_screen.png").convert() # Loads the image
                title_surf.set_colorkey((255,255,255), RLEACCEL) # Set the image's background to black to make it ~vanish~
                title_rect = title_surf.get_rect(center=(1920/2,1080/2,)) # Centers the image
                screen.blit(title_surf, title_rect) # Prepare the image to be shown on-screen
                txt = str(file)
                pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
                time_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
                time_box = time_display.get_rect() # Get bounding box
                screen.blit(time_display, time_box) # Render
                pygame.event.get()
                display.update()
            index += 1
        # print(generated_checksum) 
        full_checksum.append(generated_checksum)
    full_checksum.append(manifest.appVersion)

        # print(full_checksum)
    if full_checksum != verified_checksum or full_checksum[len(full_checksum)-1] != verified_checksum[len(verified_checksum)-1] or len(full_checksum) > len(verified_checksum): # If the checksum is longer than the verified one, it's PROBABLYYY fine
        screen.fill((0, 0, 0))
        control_surf = image.load(PATH + "/assets/missing_asset_warning.png").convert() # Loads the image
        control_surf.set_colorkey((0,0,0), RLEACCEL) # Set the image's background to black to make it ~vanish~
        control_rect = control_surf.get_rect(center=(1920/2,1080/2,)) # Centers the image
        screen.blit(control_surf, control_rect) # Prepare the image to be shown on-screen

        # mixer.music.load(PATH + "/assets/audio/fh_disclaimer_xep_trial_1.wav")
        # mixer.music.play()
        display.flip()

        waiting = True # Make the loop below run
        # Create a new clock to configure key polling rate
        polling_rate = time.Clock()

        while waiting:
            pressed_keys = key.get_pressed()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # If the Enter key is pressed, leave the controls screen
                    if (event.type == KEYDOWN) and (event.key == K_RETURN):waiting = False
                elif (event.type == JOYBUTTONDOWN and controller.get_button(10)):waiting = False

            polling_rate.tick(30)