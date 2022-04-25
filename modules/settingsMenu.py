import pygame, pygame_widgets, os, tkinter
from tkinter import messagebox
from pygame_widgets.button import Button
from modules.freddy import PATH
from modules.constants import manifest, WINDRIVE
from pygame import RLEACCEL, USEREVENT, KEYDOWN, K_RETURN, font

def settings(screen):
    stayOnScreen = True
    """SCREEN, X,Y,WID,HEIG"""
    back=Button(screen,1800,980,95,95,text='BACK',fontSize=30,margin=20,inactiveColour=(130, 100, 100),hoverColour=(200, 90, 90),pressedColour=(200, 80, 80),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 0)))

    disclaimerFile = open(PATH + "/settings/disclaimer.option", "r+")
    hideControlsFile = open(PATH + "/settings/showControls.option", "r+")
    checksumFile = open(PATH + "/settings/checksum.option", "r+")
    disclaimerFile.seek(0);hideControlsFile.seek(0);checksumFile.seek(0)

    if disclaimerFile.read()=="true": disclaimerText = "Disable Disclaimers"
    else: disclaimerText = "Enable Disclaimers"
    if hideControlsFile.read()=="true": controlsText = "Hide controls"
    else: controlsText = "Show controls"
    if checksumFile.read()=="true": checksumText = "Disable Checksums"
    else: checksumText = "Enable Checksums"

    disclaimer=Button(screen,300,300,215,95,text=disclaimerText,fontSize=30,margin=20,inactiveColour=(130, 130, 130),hoverColour=(200, 200, 200),pressedColour=(255, 255, 255),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 1)))
    controls=Button(screen,300,420,215,95,text=controlsText,fontSize=30,margin=20,inactiveColour=(130, 130, 130),hoverColour=(200, 200, 200),pressedColour=(255, 255, 255),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 2)))
    checksum=Button(screen,300,540,215,95,text=checksumText,fontSize=30,margin=20,inactiveColour=(130, 130, 130),hoverColour=(200, 200, 200),pressedColour=(255, 255, 255),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 3)))


    while stayOnScreen:
        pygame.key.get_pressed()
        for event in pygame.event.get():
            try:disclaimerFile.seek(0);hideControlsFile.seek(0);checksumFile.seek(0)
            except:NotImplemented
            if event.type == KEYDOWN:
                if event.key == K_RETURN:pygame.event.post(pygame.event.Event(USEREVENT + 0))
            elif event.type == USEREVENT + 0:
                stayOnScreen = False;back.hide();pygame_widgets.update(pygame.event.get())

            elif event.type == USEREVENT+1:
                if disclaimerFile.read()=="true":disclaimerFile.truncate();disclaimerFile.seek(0);disclaimerFile.write("false")
                else:disclaimerFile.truncate(0);disclaimerFile.seek(0);disclaimerFile.write("true")
                stayOnScreen=False;disclaimerFile.close();settings(screen)

            elif event.type == USEREVENT+2:
                if hideControlsFile.read()=="true":hideControlsFile.truncate();hideControlsFile.seek(0);hideControlsFile.write("false")
                else:hideControlsFile.truncate(0);hideControlsFile.seek(0);hideControlsFile.write("true")
                stayOnScreen=False;hideControlsFile.close();settings(screen)

            elif event.type == USEREVENT + 3:
                if checksumFile.read()=="true":checksumFile.truncate();checksumFile.seek(0);checksumFile.write("false")
                else:checksumFile.truncate(0);checksumFile.seek(0);checksumFile.write("true")
                stayOnScreen=False;checksumFile.close();settings(screen)

        screen.fill((0,0,0))

        try:
            surf = pygame.image.load(PATH + "/assets/mmenu.png").convert()
            surf.set_colorkey((0,0,0), RLEACCEL)
            rect = surf.get_rect()
            screen.blit(surf, rect)
        except:
            txt = "Image failed to load"
            pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
            time_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
            time_box = time_display.get_rect() # Get bounding box
            screen.blit(time_display, time_box) # Render

        pygame_widgets.update(pygame.event.get())
        pygame.display.update()

    back.hide();disclaimer.hide();controls.hide();checksum.hide()

    return "Done"