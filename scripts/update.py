import requests, os, sys, pygame
from pygame import font, RLEACCEL
from modules.constants import *
from threading import Thread as td

UPDATE_URL = autoUpdates.UPDATE_URL
GAME_PATH = "%s:/ProgramData/fhall"%WINDRIVE
STAGING_PATH = "%s:/ProgramData/fhall.updateStaging"%WINDRIVE
PATH = sys.path[0]
ALLOW_AUTOUPDATES = open(PATH + "/settings/autoupdate.option", "r").read()
CURRENT_VERSION = manifest.appVersion
downloadComplete = False
downloaded_binary = None

def download_binary():
    global downloadComplete, downloaded_binary

    try:
        _latestVersion = requests.get(UPDATE_URL + "/version").text
    except:
        downloadComplete = "Failed"

    if (_latestVersion != CURRENT_VERSION and _latestVersion not in autoUpdates.PAST_VERSIONS):
        try:
            downloaded_binary = requests.get(UPDATE_URL + "/fhall.dat")
            downloadComplete = True
        except:
            downloadComplete = "Failed"


def download_updates(screen):
    if ALLOW_AUTOUPDATES == False:
        return False
    else:
        title_surf = pygame.image.load(PATH + "/assets/title_screen.png").convert() # Loads the image
        title_surf.set_colorkey((255,255,255), RLEACCEL) # Set the image's background to black to make it ~vanish~
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(title_surf, title_rect) # Prepare the image to be shown on-screen

        txt = 'Checking for updates...'
        pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
        update_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
        update_box = update_display.get_rect() # Get bounding box
        update_box.bottomright=((1980,1870))
        screen.blit(update_display, update_box)

        pygame.display.update()


    while downloadComplete == False:
        for ignored in pygame.event.get():
            NotImplemented ## NOPE ##

    if (downloadComplete == "Failed"):
        title_surf = pygame.image.load(PATH + "/assets/title_screen.png").convert() # Loads the image
        title_surf.set_colorkey((255,255,255), RLEACCEL) # Set the image's background to black to make it ~vanish~
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(title_surf, title_rect) # Prepare the image to be shown on-screen

        txt = 'Update failed. Make sure GitHub is reachable.'
        pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
        update_display = pixel_font.render(txt, True, (255,100,100)) # Render the text
        update_box = update_display.get_rect() # Get bounding box
        update_box.bottomright=((1980,1870))
        screen.blit(update_display, update_box)

        pygame.display.update()

    elif downloadComplete == True:
        title_surf = pygame.image.load(PATH + "/assets/title_screen.png").convert() # Loads the image
        title_surf.set_colorkey((255,255,255), RLEACCEL) # Set the image's background to black to make it ~vanish~
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
        screen.blit(title_surf, title_rect) # Prepare the image to be shown on-screen

        txt = 'Staging app...'
        pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
        update_display = pixel_font.render(txt, True, (255,100,100)) # Render the text
        update_box = update_display.get_rect() # Get bounding box
        update_box.bottomright=((1980,1870))
        screen.blit(update_display, update_box)

        pygame.display.update()

        install_updates(screen)


def install_updates(screen):
    NotImplemented