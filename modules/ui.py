from modules.constants import * # Huh, who'd have thunk we could piggyback like this?
from modules.office.camera import PATH
from modules.networking import *
import pygame, os
from time import sleep


class fonts():
    def update(pixel_font, pixel_font_condensed, fpsCounter_font, screen, clock, camera_active, camID, power, frames, controller_connected, JOY_ID):
        """" Update font-based UI elements """

        # Time
        time = open(PATH + "/data/time", "r").read() + " AM" # Read the time
        time_display = pixel_font.render(time, True, (255,255,255)) # Render the text
        time_box = time_display.get_rect() # Get bounding box
        time_box.center = (50, 25) # Position text
        screen.blit(time_display, time_box) # Render

        # Power
        power_display = pixel_font_condensed.render(str(round(int(power))) + "%", True, (255,255,255))
        # power_display = pixel_font_condensed.render(str(pygame.mouse.get_pos()), True, (255,255,255))
        power_box = power_display.get_rect()
        power_box.center = (38, 45)
        # power_box.topleft = (38,45)
        # power_box.center = (65, 35)
        screen.blit(power_display, power_box)

        if (os.path.isfile(PATH + "/data/client")):
            draw_stat_text(pixel_font, screen, frames)

        # Camera location
        if camera_active == True: # If the camera is on, figure out which text to render
            if camID == 1:
                cloc_display = pixel_font.render("East Hall", True, (255,255,255))

            elif camID == 2:
                cloc_display = pixel_font.render("West Hall", True, (255,255,255))

            elif camID == 3:
                cloc_display = pixel_font.render("Storage Closet", True, (255,255,255))

            elif camID == 4:
                cloc_display = pixel_font.render("Dining Room", True, (255,255,255))

            elif camID == 5:
                cloc_display = pixel_font.render("Party Room", True, (255,255,255))

            elif camID == 6:
                cloc_display = pixel_font.render("Main Stage", True, (255,255,255))

            else:
                cloc_display = pixel_font.render("Unknown", True, (255,255,255))

            cloc_box = cloc_display.get_rect()
            cloc_box.topleft = (SCREEN_WIDTH-307, SCREEN_HEIGHT-300)
            screen.blit(cloc_display, cloc_box)

        if pygame.joystick.get_count() != 0:
            controller = pygame.joystick.Joystick(JOY_ID)
            pwer = controller.get_power_level()
            if (pwer != "unknown"):conpower = fpsCounter_font.render("Controller's battery: " + str(pwer).capitalize(), True, (200,235,200))
            else:conpower = fpsCounter_font.render("Controller connected", True, (200,235,200))
            conbox = conpower.get_rect()
            conbox.topright = (SCREEN_WIDTH-10,10)
            screen.blit(conpower, conbox)

            try:conname = fpsCounter_font.render(controller.get_name(), True, (230,235,100))
            except:conname = fpsCounter_font.render("No controller present", True, (230,0,0))
            cnamebox = conname.get_rect()
            cnamebox.topright = (SCREEN_WIDTH-10,35)
            screen.blit(conname, cnamebox)
        
        elif (controller_connected == True):
            conpower = fpsCounter_font.render("Controller connection lost", True, (255,0,0))
            conbox = conpower.get_rect()
            conbox.topright = (SCREEN_WIDTH-10,10)
            screen.blit(conpower, conbox)

            try:conname = fpsCounter_font.render(controller.get_name(), True, (230,235,100))
            except:conname = fpsCounter_font.render("No controller present", True, (230,0,0))
            cnamebox = conname.get_rect()
            cnamebox.topright = (SCREEN_WIDTH-10,35)
            screen.blit(conname, cnamebox)

        # Frame rate counter. This is the last thing drawn, since it should go on top.
        counterDisplay = fpsCounter_font.render(str(clock.get_fps().__round__()), True, (155,155,155))
        counterBox = counterDisplay.get_rect()
        counterBox.center = (20, SCREEN_HEIGHT - 10)
        screen.blit(counterDisplay, counterBox)

    def gameOver(font, screen):
        screen.fill((0,0,0))
        for int in range(0, 255):
            screen.fill((0,0,0))
            disp = font.render("GAME OVER", True, (int,0,0))

            dispbox = disp.get_rect()
            dispbox.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            screen.blit(disp, dispbox)
            pygame.display.flip()

            pygame.time.Clock().tick(60)

    def victory(font, screen):
        screen.fill((0,0,0))
        for pix in range(0, 8):
            screen.fill((0,0,0))
            pygame.display.flip()
            sleep(0.5)
            disp = font.render("SHIFT OVER!", True, (255,0,255))

            dispbox = disp.get_rect()
            dispbox.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            screen.blit(disp, dispbox)
            pygame.display.flip()

            sleep(0.5)
        
        cday = int(open(PATH + "/data/night", "r").read())
        data = open(PATH + "/data/night", "w")

        data.write(str(cday + 1))
        data.close

        screen.fill((0,0,0))
        pygame.display.update()
        systime.sleep(3)