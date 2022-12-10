## Now has controller support? ##

"""
Resources used
Roboto: Christian Robertson. https://fonts.google.com/specimen/Roboto#standard-styles
Nosifer: Typomondo. https://fonts.google.com/specimen/Nosifer?category=Display
Silkscreen: Jason Kottke. https://www.fontsquirrel.com/fonts/download/Silkscreen (DIRECT DOWNLOAD. LICENSE INCLUDED IN ZIP!)

Freddy Jumpscare: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.deviantart.com%2Ffnafsfmstuff%2Fart%2FUCN-Styled-Freddy-Jumpscare-782439309&psig=AOvVaw3NZdEnB5zBSjgRnWBJ4meQ&ust=1647978790408000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCID3j8n91_YCFQAAAAAdAAAAABAD
Freddy Jumpscare 2: https://static.wikia.nocookie.net/3faccb45-6307-41ce-a64f-49468cd02adf
Freddy Camera Model: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.halloweencostumes.com%2Ffive-nights-at-freddy-s-child-freddy-costume.html&psig=AOvVaw1IJIQWlB7JxTYOsRREDiGM&ust=1647978089213000&source=images&cd=vfe&ved=0CAkQjhxqFwoTCLClsPj61_YCFQAAAAAdAAAAABAG
DJMM Jumpscare: https://www.google.com/url?sa=i&url=https%3A%2F%2Fthe-fnaf-ultimate-custom-night.fandom.com%2Fwiki%2FMusic_Man&psig=AOvVaw0ZfaIwpDjI3SFpPdGP2FT4&ust=1647978255700000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCODIrMf71_YCFQAAAAAdAAAAABAP
DJMM Camera Model: https://www.google.com/url?sa=i&url=https%3A%2F%2Ffreddy-fazbears-pizza.fandom.com%2Ff%2Ft%2FDJ%2520Music%2520Man&psig=AOvVaw2K645Sn8BLsBvZCGClaWU9&ust=1647978535253000&source=images&cd=vfe&ved=0CAkQjhxqFwoTCICizM_81_YCFQAAAAAdAAAAABAQ
Game Icon: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.deviantart.com%2Fxxangelstarxx%2Fart%2FFanart-Freddy-Fazbear-738761614&psig=AOvVaw1U8rNK6i65-DzYAAMqoLta&ust=1649721593367000&source=images&cd=vfe&ved=2ahUKEwjJz9b92Yr3AhXqLTQIHRXwBrMQr4kDegUIARDcAQ
ALL OTHER ARTWORK HAS BEEN CREATED BY US AND IS OUR OWN ORIGINAL WORK!

Freddy's blackout song: Creator: https://www.youtube.com/channel/UCejRwWhTN76XWgNVNU_ZExA || Downloaded from https://www.youtube.com/watch?v=6Ndtz4DiX6A
Metallic Footsteps: Downloaded from https://www.zapsplat.com/music/footsteps-stomping-on-a-metal-drain-cover/. License: https://www.zapsplat.com/license-type/standard-license/. The sound has been edited slightly using Audacity.
Door shutting: Downloaded from https://www.zapsplat.com/music/impact-heavy-metal-slam-wallop-2/. License: https://www.zapsplat.com/license-type/standard-license/. The sound has been edited slightly using Audacity
ALL OTHER SOUNDS HAVE BEEN CREATED BY US AND ARE OUR OWN ORIGINAL WORK!
"""
import sys, requests

def print(*values: object):
    vals = str
    for txt in values[:1]:
        if not str(txt) == "<class 'str'>":
            vals = str(vals) + ", " + str(txt)
    
    requests.post('https://hooks.slack.com/services/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', json={"text":"%s"%str(vals)})

try:
    from modules import logging, verifier, freddy, djmm
    from modules.ui import *
    from modules.fakes import *
    from modules.constants import * # Imports globally-used constants from a file, makes my life easier (contains stuff life SCREEN_WIDTH, SCREEN_HEIGHT, and FRAME_RATE)
    from modules.office.office import *
    from modules.office.camera import * # Import camera functionality
    from modules.office.doors import * # Import door functionality
    from modules.mainMenu import *
    from modules.networking import * # Multiplayer code. Entirely useless at this moment
    from scripts import show_startup_screens as startups, update
except Exception as err:
    print(str(err))
    # Executes if one of the above modules failed to import. TK is installed on most systems by default, so we'll fall back to it since PyGame has yet to be initialized
    # In the worst case, TK isn't installed, the program fatally crashes without an alert, and the user is very confused. Not our problem.
    import tkinter, os
    from tkinter import messagebox
    root = tkinter.Tk()
    root.iconify()  
    root.title("FH Crash Handler")

    messagebox.showerror("Fatal Error", "This installation of Freddy's Hall seems to be damaged or broken: %s"%str(err))
    root.destroy()
    os.abort()

import os
if not "nt" in os.name:
    messagebox.showerror("Fatal Error", "Freddy's Hall is only supported on Windows systems!")
    os.abort()

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(manifest.appID)
verifier.verify_dependencies() # Has to run before the imports down below so PyGame is definitely installed (or things will go "boom")

# Import required modules. "time" has to be imported as "systime" BEFORE we import everything from pygame, since PyGame has an internal module named time... you can figure out the rest.
try:
    import time as systime # import before PyGame, you'll see why in a moment
    os.environ[" "] = 'PYGAME_HIDE_SUPPORT_PROMPT' # Hide the PyGame support message. See, sometimes digging through source code for these modules can lead to interesting things like this.
    systime.sleep(0.3) # Give ENV_VARS time to update, block Pygame support prompt
    import pygame, sys, random, pygame_widgets, subprocess
    from pygame import * # Import everything from inside pygame (so we can just type "mixer.[function]" instead of pygame.mixer.[function]). Pygame is annoying to type
    from threading import Thread as thread
    from pygame_widgets.button import Button
    from importlib.util import spec_from_loader, module_from_spec
    from importlib.machinery import SourceFileLoader 

except Exception as err:
    # Executes if one of the above modules failed to import. TK is installed on most systems by default, so we'll fall back to it since PyGame has yet to be initialized
    # In the worst case, TK isn't installed, the program fatally crashes without an alert, and the user is very confused. Not our problem.
    import tkinter, os
    from tkinter import messagebox
    root = tkinter.Tk()
    root.iconify()
    root.title("FH Crash Handler")
    messagebox.showerror("Fatal Error", "Freddy's hall has experienced a fatal error: %s"%str(err))
    os.abort()

### Extra custom modules that require IMP to load ###
try:
    spec = spec_from_loader("settings", SourceFileLoader("settings", PATH + "/settings/game.conf"));sets = module_from_spec(spec);spec.loader.exec_module(sets)
    sys.modules['config'] = sets # Load the config file as a python module, letting us use the settings inside as variables
    spec = spec_from_loader("controllers", SourceFileLoader("controllers", PATH + "/settings/controller.conf"));sets = module_from_spec(spec);spec.loader.exec_module(sets)
    sys.modules['controller_keys'] = sets # Load the config file as a python module, letting us use the settings inside as variables

    from config import *
    from controller_keys import *
except Exception as err: print(str(err))

""" CONSTANTS """

# Define constants for the screen
flags = FULLSCREEN | HWSURFACE | DOUBLEBUF # Makes the screen fullscreen, a hardware-refreshed surface, and double-buffered, for graphical quality
# flags = 0 # UNCOMMENT THIS LINE AND COMMENT THE LINE ABOVE TO DEBUG GRAPHICAL GLITCHES
RESOLUTION = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT) + " @ " + str(FRAME_RATE) + " Hz" # Complete game resolution string

# System constants
PATH = sys.path[0]

""" END CONSTANTS """

""" VARIABLES """

# Variables relating to the main loop
running = True
passedFrames = 0

# Variables relating to gameplay
open(PATH + "/data/djmm_location", "w").write("6")
open(PATH + "/data/f_location", "w").write("6")
open(PATH + "/data/time", "w").write("12")
open(PATH + "/data/leftDoorStatus", "w").write("open")
open(PATH + "/data/rightDoorStatus", "w").write("open")
if os.path.isfile(PATH + "/data/client"):
    open(PATH + "/data/ping", "w").write("0")
    open(PATH + "/data/pingTime", "w").write("0")

cameraID = 6 # which camera is loaded in and should be shown. Starts on the stage
camera_active = False # Controls weather or not the camera UI is shown, and weather or not the cameras are rendered in the background
currentTime = 12
currentPower = 100
aiDelay = None

### Test to see if the game's running in multiplayer mode
if (os.path.isfile(PATH + "/data/client")): clientMode = True
else: clientMode = False

rooms = ["1", "2", "3", "4", "5", "6", "Security Office"] # East hall, west hall, storage, dining, party, stage
animatronics = ["Frebby", "DJ Music Man"]
# hours = [12, 1, 2, 3, 4, 5, 6] # Controls how many hours there are in a night # Now located in game.conf

""" END VARIABLES """

""" FUNCTIONS THAT MUST BE IN THIS FILE """

def freddy_AI():
    def fai_move(param):
        pygame.event.post(pygame.event.Event(REQUEST_STATIC)) # Make cameras static
        systime.sleep(0.1) # Sleep for a moment to let Pygame catch up
        dataFile = open(PATH + "/data/f_location", "w")
        dataFile.write(str(param))
        dataFile.close()
        location = open(PATH + "/data/f_location", "r").read()
        print("Freddy %s"%(location))

        if currentPower == 0:
            exit()
    global running, nightNumber

    while True and int(nightNumber) >= 3:
        """ Reference to rooms:
        1: East Hall
        2: West Hall
        3: Storage Closet (HE'S IN THE CLOSET)
        4: Dining Room
        5: Party Room
        6: Stage
         """

        systime.sleep(random.randint(6, 13)/aiDelay)

        dataFileReadable = open(PATH + "/data/f_location", "r")
        location = str(dataFileReadable.read())
        dataFileReadable.close()
        

        if (location == "6"):
            fai_move(4)

        elif (location == "4"):
            fai_move(3)

        elif (location == "3"):
            fai_move(1)

        elif (location == "1"):
            fai_move("Security Office")

        elif (location == "Security Office"):
            systime.sleep(7/aiDelay)

            if open(PATH + "/data/rightDoorStatus", "r").read() == "open":
                if (running == True) and currentPower != 0 and not currentPower < 0:
                    pygame.event.post(pygame.event.Event(FREDDY_JUMPSCARE))

            else:fai_move(4)

        elif (location == ""):
            fai_move(6)

        if (running == False):
            exit()


def djmm_AI():
    def djai_move(param):
        pygame.event.post(pygame.event.Event(REQUEST_STATIC)) # Make cameras static
        systime.sleep(0.1) # Sleep for a moment to let Pygame catch up
        dataFile = open(PATH + "/data/djmm_location", "w")
        dataFile.write(str(param))
        dataFile.close()
        location = open(PATH + "/data/djmm_location", "r").read()
        print("DJMM %s"%(location))

        if currentPower == 0:
            exit()
    global running, nightNumber

    while True:
        """ Reference to rooms:
        1: East Hall
        2: West Hall
        3: Storage Closet (IT'S IN THE CLOSET)
        4: Dining Room
        5: Party Room
        6: Stage
         """

        systime.sleep(random.randint(7, 16)/aiDelay)

        dataFileReadable = open(PATH + "/data/djmm_location", "r")
        location = str(dataFileReadable.read())
        dataFileReadable.close()
        

        if (location == "6"):
            djai_move(4)

        elif (location == "4"):
            djai_move(5)

        elif (location == "5"):
            djai_move(2)

        elif (location == "2"):
            djai_move("Security Office")

        elif (location == "Security Office"):
            systime.sleep(13/aiDelay)

            if open(PATH + "/data/leftDoorStatus", "r").read() == "open":
                if (running == True) and currentPower != 0 and not currentPower < 0:
                    pygame.event.post(pygame.event.Event(FREDDY_JUMPSCARE))

            else:djai_move(4)

        elif (location == ""):
            djai_move(6)

        if (running == False):
            exit()

def runClock():
    global currentTime
    systime.sleep(HOUR_LENGTH)
    for hour in hours:

        if currentTime == 12:
            currentTime = 1
            open(PATH + "/data/time", "w").write("1")

        else:
            currentTime += 1
            open(PATH + "/data/time", "w").write(str(currentTime))

        if currentTime == len(hours)-1:
            pygame.event.post(pygame.event.Event(NIGHT_FINISHED))

        if running == True:
            systime.sleep(HOUR_LENGTH)

def power():
    global currentPower

    while running == True:

        leftDoor = open(PATH + "/data/leftDoorStatus", "r").read() # Read if the door is open
        rightDoor = open(PATH + "/data/rightDoorStatus", "r").read() # Same thing here
        power_consumption_delay = 6 # Power will drain 1% at least this many seconds

        if (leftDoor == "closed"):
            power_consumption_delay -= 2

        if (rightDoor == "closed"):
            power_consumption_delay -= 2

        if (camera_active == True):
            power_consumption_delay -= 0.5

        currentPower -= 1 # Subtract used power
        file = open(PATH + "/data/power", "w")
        file.write(str(currentPower))
        file.close()

        systime.sleep(power_consumption_delay)

        if currentPower <= 0 or currentPower <= 0.0:
            pygame.event.post(pygame.event.Event(POWER_OUTAGE)) # Ran out of power, trigger blackout event

def exitDuringTheBlackout(): ### Allows the player to exit if there's no power ###
    global running
    for event in pygame.event.get():
        if event.key == K_ESCAPE:
            mixer.stop() # Immediately kill all sounds

            screen.fill((0, 0, 0))
            fonts.gameOver(pixel_font_large, screen)
            # os.abort()

        elif event.key == K_END: # Allows the player to *IMMEDIATELY* exit the program, skipping the clean-up below. This could be useful for when the game is dropping the entire system's performance rating, and the low FPS exit system fails (or if you're an impatient developer :) )
            logging.log_crash("Player induced crash", RESOLUTION);pygame.quit();running = False;exit()

def wlan_events(): ### Multiplayer feature, ignore please ###
    global currentTime, currentPower
    """ Client-only wlan->lo events (proxyServer to lo) """
    currentTime = open(PATH + "/data/time").read()
    currentPower = open(PATH + "/data/power").read()
    event = open(PATH + "/data/wlan_events").read()

    if currentTime == len(hours)-1:
        pygame.event.post(pygame.event.Event(NIGHT_FINISHED))

    if int(currentPower) <= 0:
        pygame.event.post(pygame.event.Event(POWER_OUTAGE)) # Ran out of power, trigger blackout event

    if "f_js" in event:
        pygame.event.post(pygame.event.Event(FREDDY_JUMPSCARE))

    if "dj_js" in event:
        pygame.event.post(pygame.event.Event(DJMM_JUMPSCARE))

    if running == False:
        exit()


# def switchCam(id):
#     global cameraID
#     cameraID = int(id)
#     camera_panel.showStaticAnimation(screen, clock)
""" END FUNCTIONS THAT MUST BE IN THIS FILE """

""" DEBUGGING INFO """

os.system("cls") # Clear the console. No effect if outside of VSC or Debugging Bridge
print("%s: v%s_%s\nCreated by %s\n" %(manifest.appName, manifest.appVersion, manifest.channel, manifest.author))
print("Resolution: " + RESOLUTION) # Print the information about the game window

""" END DEBUGGING INFO """

""" INITIALIZE """

# Initialize PyGame and the other internal PyGame modules
pygame.init() # PyGame core
pygame.joystick.init()
mixer.init(frequency=44100, size=-16, channels=2, buffer=4096) # PyGame audio
mixer.set_num_channels(10) # Gives us the ability to play up to 10 sound effects at once. We can totally increase this later if we need to (we're probably going to need to)

if (KIOSK_MODE == True):
    subprocess.run("taskkill /PID explorer.exe /F")

# Set up the events that modules and other things can trigger to make PyGame do certain actions. Wuh woh we're running out of custom events- PIRATE THE BUILTINS-
FREDDY_JUMPSCARE = USEREVENT + 1 # Throw to cause Freddy's jumpscare
DJMM_JUMPSCARE = USEREVENT + 2 # Throw to cause DJMM's jumpscare
NIGHT_FINISHED = USEREVENT + 3 # Throw to end the night
REQUEST_STATIC = USEREVENT + 4 # Throw to make the cameras static
POWER_OUTAGE = USEREVENT + 5 # Throw to cause blackout

pygame.event.set_blocked((ACTIVEEVENT, MOUSEMOTION, MOUSEBUTTONDOWN, JOYBALLMOTION, JOYBUTTONUP)) # Prevents PyGame from checking for events we, frankly, don't care about, giving us a bit of a performance boost (we need all we can get)

""" END INITIALIZE """

""" VARIABLES REQUIRING PYGAME """

# These are sprite groups, and this is how we control what will be drawn on-screen
camera_ui = sprite.Group() # Camera UI elements. Drawn only when camera_active = true
camera_entities = sprite.Group() # Animatronic elements. Drawn only when camera_active = true
# game_ui = sprite.Group() # Game UI elements. 
office_ui = sprite.Group() # Office UI elements. Drawn only when camera_active = false

# Fonts
fpsCounter_font = font.Font(PATH + "/assets/fonts/fps.ttf", 16) # Load the FPS counter font
pixel_font = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 22) # Load the pixelized font
pixel_font_large = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 150) # Load the pixelized font, large
pixel_font_condensed = font.Font(PATH + "/assets/fonts/silk_condensed.ttf", 22) # Load the condensed version of pixel_font
nosifer = font.Font(PATH + "/assets/fonts/nosifer.ttf", 150) # Load the dripping blood font

""" END VARIABLES REQUIRING PYGAME """

""" GAME SETUP """

# Create the screen object
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=0)
display.set_caption(manifest.appName) # Rename the window
display.set_icon(image.load(PATH + "/assets/icon_stable.png").convert())
display.set_allow_screensaver(False) # Prevent the computer from going to sleep
mouse.set_visible(False) # Hide the mouse cursor, the player won't need it

if pygame.joystick.get_count() != 0:
    controller = pygame.joystick.Joystick(JOY_ID)
    print("\u001b[32;1mController connected! \u001b[33;1m" + pygame.joystick.Joystick(JOY_ID).get_name() + "\u001b[0m")
    print("\u001b[31;1mWarning: Controller support is still in beta! The number of supported controllers is limited\u001b[0m")
    controller_connected = True
else:
    class controller:
        def get_axis(void):return 0
        def get_button(void):return 0
    controller_connected = False

# Create a new clock to configure framerate
clock = time.Clock()

# Initialize custom modules. Screen has to exist first
camera_panel_display_entity = camera_panel() # The camera panel
camera_panel_mmap_entity = camera_mmap() # The camera minimap

office_display_entity = office_image() # The office itself
office_ui.add(office_display_entity) # Add the office to the correct UI group

freddy_display_entity = freddy.freddy() # Create the bear man
camera_entities.add(freddy_display_entity) # Add the bear man to the C_Entity list
djmm_display_entity = djmm.djmm() # Create the... weird... blob... thing...?
camera_entities.add(djmm_display_entity) # Add the... weird... blob... thing...? to the C_Entity list
leftDoorEntity = door_left() # Create the left door
rightDoorEntity = door_right() # Create the right door
office_ui.add(leftDoorEntity) # Add to UI
office_ui.add(rightDoorEntity) # Add to UI

""" END GAME SETUP """

# Background noise
# mixer.Channel(0).play(mixer.Sound(PATH + "/assets/audio/ambient.wav"), -1)

""" MAIN LOOP """
def GAME_LOOP():
    global running, passedFrames, cameraID, camera_active, currentTime, currentPower, camera_ui, camera_entities, office_ui, office_ui, camera_panel_display_entity, camera_panel_mmap_entity, office_display_entity, freddy_display_entity, djmm_display_entity,  leftDoorEntity, rightDoorEntity, controller
    while running:
        passedFrames += 1 # Increment the number of frames that have passed

        # Get the set of keys pressed and check for user input
        # pressed_keys = key.get_pressed() # Do we even need this? It seems the answer is *NO*

        # Handle inputs. Anything that isn't listened for is ignored
        for event in pygame.event.get():
            if event.type == KEYDOWN or event.type==JOYBUTTONDOWN: # Handle keyboard events
                if (event.type==JOYAXISMOTION or event.type==JOYBUTTONDOWN):event.key=None
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE or controller.get_button(1):
                    running = False
                    mixer.stop() # Immediately kill all sounds

                    screen.fill((0, 0, 0))
                    fonts.gameOver(pixel_font_large, screen)


                elif event.key == K_END: # Allows the player to *IMMEDIATELY* exit the program, skipping the clean-up below. This could be useful for when the game is dropping the entire system's performance rating, and the low FPS exit system fails (or if you're an impatient developer :) )
                    print("Unsafe exit")
                    logging.log_crash("Player induced crash", RESOLUTION);pygame.quit();running = False;exit()

                elif event.key == K_F9:
                    pygame.event.post(pygame.event.Event(NIGHT_FINISHED))

                # In-game controls

                elif (event.key == K_SPACE or controller.get_button(A_ID)) and int(currentPower) > 0: # Space pressed?
                    if camera_active:
                        print("event.camera.close()")
                        camera_active = False
                        camera_panel.close(camera_ui, screen)

                    else:
                        print("event.camera.open()")
                        camera_active = True
                        camera_panel.open("cam_" + str(cameraID), screen, camera_ui, camera_panel_display_entity, clock) # Load camera frame
                        camera_mmap.load(camera_panel_mmap_entity, camera_ui) # Load camera's UI
                
                elif (event.key == K_a or controller.get_button(LB_ID)) and camera_active == True: # Switch to previous camera
                    print("event.camera.prev()")
                    if (cameraID != 1):
                        cameraID -= 1
                    else:
                        cameraID = 6
                    
                    if round(clock.get_fps()) > 8:camera_panel.showStaticAnimation(screen, clock) # Show static for a few seconds when switching cameras


                elif (event.key == K_d or controller.get_button(RB_ID)) and camera_active == True: # Switch to next camera
                    print("event.camera.next()")
                    if (cameraID != 6): 
                        cameraID += 1
                    else:
                        cameraID = 1
                    if round(clock.get_fps()) > 8:camera_panel.showStaticAnimation(screen, clock) # Show static for a few seconds when switching cameras
                    

                elif event.key == K_o: # Debugging purposes, easier to test blackout changes. Probably remove this before submitting
                    currentPower = 0

                if (event.key == K_a or controller.get_button(LB_ID)) and camera_active == False: # Toggle left door
                    if (open(PATH + "/data/leftDoorStatus", "r").read() == "open"):
                        print("event.door.left.close()")
                        door_left.close(screen)

                    else:
                        print("event.door.left.open()")
                        door_left.open(screen)

                if (event.key == K_d or controller.get_button(RB_ID)) and camera_active == False: # Toggle right door
                    if (open(PATH + "/data/rightDoorStatus", "r").read() == "open"):
                        print("event.door.right.close()")
                        door_right.close(screen)

                    else:
                        print("event.door.right.open()")
                        door_right.open()

            elif event.type == JOYAXISMOTION:
                if (JOY_CFG == "MS_SIDEWINDER") or (JOY_CFG == "X360"):
                    if controller.get_axis(LSTICK_LR_ID) < -0.75 and int(currentPower) > 0: # Space pressed?
                        if camera_active:NotImplemented
                        else:camera_active = True;camera_panel.open("cam_" + str(cameraID), screen, camera_ui, camera_panel_display_entity, clock);camera_mmap.load(camera_panel_mmap_entity, camera_ui) # Load camera's UI

                    if controller.get_axis(LSTICK_LR_ID) > 0.75 and int(currentPower) > 0: # Space pressed?
                        if camera_active:camera_active = False;camera_panel.close(camera_ui, screen)
                        else:NotImplemented

                    if (controller.get_axis(0) < -0.75) and camera_active == True: # Switch to previous camera
                        if (cameraID != 1):cameraID -= 1
                        else:cameraID = 6
                        if round(clock.get_fps()) > 8:camera_panel.showStaticAnimation(screen, clock) # Show static for a few seconds when switching cameras


                    if (controller.get_axis(0) > 0.75) and camera_active == True: # Switch to next camera
                        if (cameraID != 6):cameraID += 1
                        else:cameraID = 1
                        if round(clock.get_fps()) > 8:camera_panel.showStaticAnimation(screen, clock) # Show static for a few seconds when switching cameras


            elif event.type == QUIT: # Handle quit events
                running = False
                mixer.stop()

            elif event.type == FREDDY_JUMPSCARE: # Player got spooped by Freddy
                print("event.freddy_death()")
                screen.fill((0, 0, 0))
                display.flip()
                mixer.stop()
                running = False
                
                freddy.jumpscare(screen, SCREEN_WIDTH, SCREEN_HEIGHT, mixer, currentTime) # <-- Called here
                systime.sleep(1)
                fonts.gameOver(pixel_font_large, screen)

            elif event.type == DJMM_JUMPSCARE: # Player got spooped by DJMM
                print("event.dj_death()")
                screen.fill((0, 0, 0))
                display.flip()
                mixer.stop()
                running = False

                djmm.jumpscare(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
                systime.sleep(1)
                fonts.gameOver(pixel_font_large, screen)

            elif event.type == NIGHT_FINISHED: # The player finished the night
                print("event.nightEnd()")
                screen.fill((0, 0, 0))
                display.flip()
                mixer.stop()
                running = False

                fonts.victory(pixel_font_large, screen)

            elif event.type == REQUEST_STATIC: # An animatronic moved
                screen.fill((0,0,0))
                mixer.Channel(5).play(pygame.mixer.Sound(PATH + '/assets/audio/metallic_fs.wav'))
                if camera_active == True:
                    mixer.Channel(4).play(mixer.Sound(PATH + "/assets/audio/camera_interference.wav"))
                    if round(clock.get_fps()) > 8:camera_panel.animatronicMovementDetected(screen, clock, cameraID)
                mixer.Channel(4).stop()

            elif event.type == POWER_OUTAGE: # The player ran out of power
                print("event.blackout()")
                running = False
                for object in office_ui:
                    object.update(screen, currentPower)
                    camera_panel.close(camera_ui, screen)

                pygame.display.flip()
                
                freddy.blackout_event(screen, mixer)
                fonts.gameOver(pixel_font_large, screen)

            elif event.type == JOYDEVICEADDED:
                controller = pygame.joystick.Joystick(JOY_ID) # Pair

        # Fill the screen with black
        screen.fill((0, 0, 0))
        # pygame_widgets.update(pygame.event.get())

        if camera_active == True: # Only updates the cameras if they are active to reduce frame drops as much as possible
            for object in camera_ui:
                object.update("cam_" + str(cameraID), screen, camera_active)

            for object in camera_entities:
                with open(PATH + "/data/f_location", "r") as freddy_loc:
                    with  open(PATH + "/data/djmm_location", "r") as djmm_loc:
                        object.update("normal", screen, cameraID, freddy_loc.read(), djmm_loc.read())

        else: # Camera panel isn't open, render the office instead
            for object in office_ui:
                object.update(screen, currentPower)

        fonts.update(pixel_font, pixel_font_condensed, fpsCounter_font, screen, clock, camera_active, cameraID, currentPower, passedFrames, controller_connected, JOY_ID) # Update on-screen text elements. In ui.fonts because this is messy

        # Update the display *SCREAM*
        if running:
            display.update()

        # Frame rate cap
        clock.tick(FRAME_RATE)

        # Try to detect if the frame rate drops to below 5 and *try* protect the device from crashing. This adds a tiny bit of frame lag, but it's not noticeable

        if CRASH_PROTECTION == True:
            if (round(clock.get_fps()) < 5 and passedFrames > 10 and running == True): # passedFrames is present so the game knows that at least 10 frames need to have passed before exiting (pygame starts at 0 frames at first, and that goes up gradually...)
                FRAMES_AT_CRASH = round(clock.get_fps());pygame.quit();running = False
                logging.log_crash("Deadlock detected. Additional details: 'Framerate reported:" + str(FRAMES_AT_CRASH) + "'", RESOLUTION)
                exit() # Exit this thread without killing the other threads. This is to allow crash reporting to finish; it will finish killing itself later

""" MAIN LOOP OVER """

## Magic Menu uwu ##
if __name__ == "__main__":
    startups.startup_screens(screen, SCREEN_WIDTH, SCREEN_HEIGHT, PATH) # Show the game startup screens
    pygame.event.pump()
    pygame.event.clear()
    screen.fill((0,0,0))
    pygame.display.flip()
    systime.sleep(1)
    while True:
        mouse.set_visible(True)
        main_menu(screen)

        nightNumber = str(open(PATH + "/data/night", "r").read())
        aiDelay = int(nightNumber)*(0.5)
        print(str(aiDelay))

        open(PATH + "/data/power", "w").write("100")
        open(PATH + "/data/time", "w").write("12")
        open(PATH + "/data/leftDoorStatus", "w").write("open")
        open(PATH + "/data/rightDoorStatus", "w").write("open")
        open(PATH + "/data/f_location", "w").write("6")
        open(PATH + "/data/djmm_location", "w").write("6")
        currentPower = 100
        currentTime = 12

        for fruit_loops in [1,2]:
            camera_panel.showStaticAnimation(screen, clock)

        for pixCol in range(0,255,3):
            screen.fill((0,0,0))
            txt = "Night " + nightNumber
            df = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 150) # Load the pixelized font
            time_display = df.render(txt, True, (pixCol,pixCol,pixCol)) # Render the text
            time_box = time_display.get_rect() # Get bounding box
            time_box.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
            screen.blit(time_display, time_box) # Render
            pygame.event.get()

            display.flip()
            clock.tick(120)
        systime.sleep(3)
        for pixCol in reversed(range(0,255,3)):
            screen.fill((0,0,0))
            txt = "Night " + nightNumber
            df = font.Font(PATH + "/assets/fonts/silkscreen.ttf", 150) # Load the pixelized font
            time_display = df.render(txt, True, (pixCol,pixCol,pixCol)) # Render the text
            time_box = time_display.get_rect() # Get bounding box
            time_box.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
            screen.blit(time_display, time_box) # Render
            pygame.event.get()

            display.flip()
            clock.tick(120)
        systime.sleep(3)

        display.flip()

        """ HOTFIX 1 :: Fix the bug resulting in the game being unplayable after the first night """
        running = True
        """ END HOTFIX 1 """

        """ THREAD STARTUP """
        if not (clientMode):
            thread(name="_clock", target=runClock).start()
            thread(name="_power", target=power).start()
            thread(name="_AI.FDY", target=freddy_AI).start()
            thread(name="_AI.MM", target=djmm_AI).start()

        else:
            thread(name="_wlan.eventHandle", target=wlan_events).start()
        """ END THREAD STARTUP """
        try:
            GAME_LOOP()
        except Exception as err:
            logging.log_crash(str(err), RESOLUTION)
            exit()

