import pygame, pygame_widgets, os, tkinter
from tkinter import messagebox
from pygame_widgets.button import Button
from modules.freddy import PATH
from modules.constants import manifest, WINDRIVE
from pygame import RLEACCEL, USEREVENT, KEYDOWN, K_RETURN, font

def about(screen):
    stayInMenu = True
    while stayInMenu:
        pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:pygame.event.post(pygame.event.Event(USEREVENT + 0))
            elif event.type == USEREVENT + 0:
                stayInMenu = False
        screen.fill((0,0,0))

        try:
            surf = pygame.image.load(PATH + "/assets/credits.png").convert()
            surf.set_colorkey((0,0,0), RLEACCEL)
            rect = surf.get_rect()
            screen.blit(surf, rect)
        except:
            txt = "About can't be loaded. Press ENTER to return to menu"
            pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
            time_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
            time_box = time_display.get_rect() # Get bounding box
            screen.blit(time_display, time_box) # Render

        pygame.display.update()

    return "Done"

def uninstall(screen):
    stayInMenu = True
    u=Button(screen,(1920/2)-107.5,(1080/2-200),215,95,text='UNINSTALL',fontSize=50,margin=20,inactiveColour=(135, 100, 100),hoverColour=(255, 0, 0),pressedColour=(255, 0, 0),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 1)))
    c=Button(screen,(1920/2)-107.5,(1080/2-200)+105,215,95,text='CANCEL',fontSize=50,margin=20,inactiveColour=(100, 100, 100),hoverColour=(90, 200, 90),pressedColour=(90, 255, 90),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 0)))

    while stayInMenu:
        pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == USEREVENT + 0:
                stayInMenu == False
                u.hide();c.hide()
                return None
            elif event.type == USEREVENT + 1:
                os.startfile(WINDRIVE + ":/ProgramData/fhall/uninstall.py")
                os.abort()
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

        txt = "ARE YOU SURE?"
        pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 150) # Load the pixelized font
        time_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
        time_box = time_display.get_rect() # Get bounding box
        time_box.center=(1920/2,1080/2 -300)
        screen.blit(time_display, time_box) # Render

        pygame_widgets.update(pygame.event.get())
        pygame.display.update()

    u.hide();c.hide()
    return None

def quitGame():
    # This code will only be run after the main loop has exited safely (didn't crash)
    print("Cleaning up...")

    ## Reset all variables, no sneaky hacking >:) ##
    open(PATH + "/data/djmm_location", "w").write("6")
    open(PATH + "/data/f_location", "w").write("6")
    open(PATH + "/data/time", "w").write("12")
    open(PATH + "/data/leftDoorStatus", "w").write("open")
    open(PATH + "/data/rightDoorStatus", "w").write("open")
    os.abort()



def main_menu(screen):
    stayInMenu = True
    multimode = os.path.isfile(PATH + "/data/client")

    """SCREEN, X,Y,WID,HEIG"""
    if not multimode:p=Button(screen,1700,200,150,95,text='PLAY',fontSize=50,margin=20,inactiveColour=(100, 100, 100),hoverColour=(90, 200, 90),pressedColour=(200, 0, 0),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 0)))
    else:p=Button(screen,1700,200,150,95,text='JOIN',fontSize=50,margin=20,inactiveColour=(100, 130, 0),hoverColour=(90, 200, 90),pressedColour=(200, 0, 0),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 0)))
    e=Button(screen,1700,350,150,95,text='EXIT',fontSize=50,margin=20,inactiveColour=(100, 100, 100),hoverColour=(200, 90, 90),pressedColour=(90, 90, 90),radius=20,onClick=lambda: quitGame())
    a=Button(screen,1700,500,150,95,text='ABOUT',fontSize=50,margin=20,inactiveColour=(100, 100, 100),hoverColour=(200, 90, 90),pressedColour=(90, 90, 90),radius=20,onClick=lambda: about(screen))
    u=Button(screen,1700,650,150,95,text='UNINSTALL',fontSize=30,margin=20,inactiveColour=(130, 100, 100),hoverColour=(200, 90, 90),pressedColour=(255, 255, 255),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 1)))

    while stayInMenu == True:
        for event in pygame.event.get():
            if event.type == USEREVENT + 0:
                stayInMenu = False
                u.hide();a.hide();e.hide(); p.hide()

            elif event.type == USEREVENT + 1:
                screen.fill((0,0,0))
                u.hide();a.hide();e.hide(); p.hide()
                uninstall(screen)
                u.show();a.show();e.show(); p.show()


        screen.fill((0,0,0))

        try:
            surf = pygame.image.load(PATH + "/assets/mmenu.png").convert()
            surf.set_colorkey((0,0,0), RLEACCEL)
            rect = surf.get_rect()
            screen.blit(surf, rect)
        except:
            txt = "Menu can't be loaded. There might be something wrong with your installation"
            pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
            time_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
            time_box = time_display.get_rect() # Get bounding box
            screen.blit(time_display, time_box) # Render

        txt = "Freddy's Hall %s %s. Copyright %s 2022"%(manifest.appVersion, manifest.channel, manifest.author)
        pixel_font = font.Font(PATH + "/assets/fonts/fps.ttf", 22)
        vinfo_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
        vinfo_box = vinfo_display.get_rect() # Get bounding box
        vinfo_box.bottomleft=(5, 1075)
        screen.blit(vinfo_display, vinfo_box) # Render

        pygame_widgets.update(pygame.event.get())
        pygame.display.update()

    pygame.mouse.set_visible(False)