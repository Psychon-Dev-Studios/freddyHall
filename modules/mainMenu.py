import pygame, pygame_widgets, os, tkinter, time as systime, sys, subprocess
from tkinter import messagebox
from pygame_widgets.button import Button
from modules.fakes import *
from modules.freddy import PATH
from modules.settingsMenu import *
from modules.constants import manifest, WINDRIVE
from pygame import RLEACCEL, USEREVENT, KEYDOWN, K_RETURN, font
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
try:
    spec = spec_from_loader("settings", SourceFileLoader("settings", PATH + "/settings/game.conf"))
    sets = module_from_spec(spec)
    spec.loader.exec_module(sets)
    sys.modules['config'] = sets
    spec = spec_from_loader("controllers", SourceFileLoader("controllers", PATH + "/settings/controller.conf"));sets = module_from_spec(spec);spec.loader.exec_module(sets)
    sys.modules['controller_keys'] = sets # Load the config file as a python module, letting us use the settings inside as variables    

    from config import *
    from controller_keys import *
except:NotImplemented

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
    if (KIOSK_MODE == True):
        subprocess.call("explorer.exe")
    return None

def quitGame(p,s,e,a,u):
    u.hide();a.hide();e.hide(); p.hide();s.hide()
    systime.sleep(0.2)
    pygame.display.update()
    # This code will only be run after the main loop has exited safely (didn't crash)
    print("Cleaning up...")

    ## Reset all variables, no sneaky hacking >:) ##
    open(PATH + "/data/djmm_location", "w").write("6")
    open(PATH + "/data/f_location", "w").write("6")
    open(PATH + "/data/time", "w").write("12")
    open(PATH + "/data/leftDoorStatus", "w").write("open")
    open(PATH + "/data/rightDoorStatus", "w").write("open")
    if (KIOSK_MODE == True):
        subprocess.run("explorer.exe")
    os.abort()



def main_menu(screen):
    stayInMenu = True
    multimode = os.path.isfile(PATH + "/data/client")
    pygame.mixer.music.load(PATH + "/assets/audio/mmenu_loop-temp2.wav")
    pygame.mixer.music.play(-1, fade_ms=3000)

    if pygame.joystick.get_count() != 0:
        controller = pygame.joystick.Joystick(JOY_ID)
    else:
        class controller:
            def get_axis(void):return 0
            def get_button(void):return 0

    if pygame.joystick.get_count() != 0:cplay = " (A)";cexit = " (B)"
    else:cplay="";cexit=""

    """SCREEN, X,Y,WID,HEIG"""
    if not multimode:p=Button(screen,1700,200,150,95,text='PLAY%s'%(cplay),fontSize=50,margin=20,inactiveColour=(180, 180, 180),hoverColour=(230, 230, 230),pressedColour=(180, 200, 180),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 0)))
    else:p=Button(screen,1700,200,150,95,text='JOIN%s'%(cplay),fontSize=50,margin=20,inactiveColour=(180, 180, 100),hoverColour=(230, 230, 230),pressedColour=(180, 200, 180),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 0)))
    s=Button(screen,1700,350,150,95,text='OPTIONS',fontSize=40,margin=20,inactiveColour=(180, 180, 180),hoverColour=(230, 230, 230),pressedColour=(180, 200, 180),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 2)))
    e=Button(screen,1700,500,150,95,text='EXIT%s'%(cexit),fontSize=50,margin=20,inactiveColour=(200, 180, 180),hoverColour=(255, 230, 230),pressedColour=(90, 90, 90),radius=20,onClick=lambda: quitGame(p,s,e,a,u))
    a=Button(screen,1700,650,150,95,text='ABOUT',fontSize=50,margin=20,inactiveColour=(180, 180, 180),hoverColour=(230, 230, 230),pressedColour=(180, 200, 180),radius=20,onClick=lambda: about(screen))
    u=Button(screen,1700,800,150,95,text='UNINSTALL',fontSize=30,margin=20,inactiveColour=(180, 150, 150),hoverColour=(200, 90, 90),pressedColour=(255, 255, 255),radius=20,onClick=lambda: pygame.event.post(pygame.event.Event(USEREVENT + 1)))

    if KIOSK_MODE == True:
        e.hide()
        u.hide()
        s.hide()

    while stayInMenu == True:
        for event in pygame.event.get():
            if event.type == USEREVENT + 0:
                stayInMenu = False
                u.hide();a.hide();e.hide(); p.hide();s.hide()

            elif event.type == USEREVENT + 1:
                screen.fill((0,0,0))
                u.hide();a.hide();e.hide(); p.hide();s.hide()
                uninstall(screen)
                a.show();p.show()

                if KIOSK_MODE == False:
                    e.show(); u.show();s.show()

            elif event.type == USEREVENT + 2:
                u.hide();a.hide();e.hide(); p.hide();s.hide()
                settings(screen)
                a.show(); p.show()
                if KIOSK_MODE == False:
                    e.show(); u.show();s.show()

        if (controller.get_button(A_ID)):stayInMenu = False;u.hide();a.hide();e.hide(); p.hide();s.hide();pygame_widgets.update(pygame.event.get());pygame.display.update()

        elif (controller.get_button(B_ID)):u.hide();a.hide();e.hide(); p.hide();s.hide();pygame_widgets.update(pygame.event.get());pygame.display.update();quitGame(p,s,e,a,u)

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

        if (manifest.isSuperSecretBuild == True):
            txt = "Super-secret developer's build - DO NOT DISTRIBUTE!"
            pixel_font = font.Font(PATH + "/assets/fonts/fps.ttf", 22)
            vinfo_display = pixel_font.render(txt, True, (255,0,0)) # Render the text
            vinfo_box = vinfo_display.get_rect() # Get bounding box
            vinfo_box.bottomleft=(5, 1035)
            screen.blit(vinfo_display, vinfo_box) # Render

        if (KIOSK_MODE == True):
            txt = "Kiosk Mode"
            pixel_font = font.Font(PATH + "/assets/fonts/fps.ttf", 22)
            vinfo_display = pixel_font.render(txt, True, (255,255,255)) # Render the text
            vinfo_box = vinfo_display.get_rect() # Get bounding box
            vinfo_box.bottomright=(1915, 1075)
            screen.blit(vinfo_display, vinfo_box) # Render

        pygame_widgets.update(pygame.event.get())
        pygame.display.update()

    pygame.mixer.music.fadeout(2)
    pygame.mouse.set_visible(False)