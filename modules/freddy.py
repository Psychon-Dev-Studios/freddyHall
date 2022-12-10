""" 
They call me Freddy, so just follow MY LEAD~~\n
Freddy-related modules
"""

import pygame
from pygame import *
import sys, os, random
from time import sleep
PATH = sys.path[0]

from modules.constants import *

clock = pygame.time.Clock()



def jumpscare(screen, SCREEN_WIDTH, SCREEN_HEIGHT, mixer: pygame.mixer, time): # Almost same code as DJMM
    "Show Froody's jumpscare"
    
    frameLooped = 0 # How many times the animation has looped

    if not (time >= 3 and not time == 12) or time <= 2:
        mixer.Channel(1).play(pygame.mixer.Sound(PATH + '/assets/audio/cxr_jumpscare_2.wav')) # Play the jumpscare sound
        while frameLooped < 24: # loop 24 times
            for frame in os.listdir(PATH + "/assets/ffaz/frames"):
                screen.fill((0,0,0)) # Blank out the screen

                if (".gif" in frame or ".png" in frame): # Makes sure the file is a valid image
                    surf = pygame.image.load(PATH + "/assets/ffaz/frames/%s"%frame).convert() # Loads the image
                    surf.set_colorkey((0,0,0), RLEACCEL) # Configures the image to be processed at full RGB spectrum at low quality (for speed)
                    rect = surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
                    screen.blit(surf, rect) # Prepare the image to be shown on-screen
                    pygame.event.get()

                    pygame.display.flip() # Update the screen
                    frameLooped += 1 # Update how many times the animation has looped
                    clock.tick(60) # Limit to 60 FPS
    
    else:
        mixer.Channel(1).play(pygame.mixer.Sound(PATH + '/assets/audio/fdy_dm_js.wav')) # Play the jumpscare sound
        while frameLooped < 24: # loop 24 times
            for frame in os.listdir(PATH + "/assets/ffaz/frames_demonic"):
                screen.fill((0,0,0)) # Blank out the screen

                if (".gif" in frame or ".png" in frame): # Makes sure the file is a valid image
                    surf = pygame.image.load(PATH + "/assets/ffaz/frames_demonic/%s"%frame).convert() # Loads the image
                    surf.set_colorkey((0,0,0), RLEACCEL) # Configures the image to be processed at full RGB spectrum at low quality (for speed)
                    rect = surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
                    screen.blit(surf, rect) # Prepare the image to be shown on-screen
                    pygame.event.get()

                    pygame.display.flip() # Update the screen
                    frameLooped += 1 # Update how many times the animation has looped
                    clock.tick(60) # Limit to 60 FPS

        frameLooped = 0
        while frameLooped < 20:
            screen.fill((0,0,0))
            surf = pygame.image.load(PATH + "/assets/ffaz/frames_demonic/frame_10_delay-0.04s.gif").convert() # Loads the image
            surf.set_colorkey((0,0,0), RLEACCEL) # Configures the image to be processed at full RGB spectrum at low quality (for speed)
            rect = surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
            screen.blit(surf, rect) # Prepare the image to be shown on-screen
            pygame.event.get()
            pygame.display.flip() # Update the screen

            screen.fill((0,0,0))
            surf = pygame.image.load(PATH + "/assets/ffaz/frames_demonic/frame_09_delay-0.04s.gif").convert() # Loads the image
            surf.set_colorkey((0,0,0), RLEACCEL) # Configures the image to be processed at full RGB spectrum at low quality (for speed)
            rect = surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
            screen.blit(surf, rect) # Prepare the image to be shown on-screen
            pygame.event.get()
            pygame.display.flip() # Update the screen
            frameLooped += 1 # Update how many times the animation has looped
            clock.tick(60) # Limit to 60 FPS


def blackout_event(screen, mixer):
    """ The power went out """
    animation_frame_rate = 30 # the frame rate the animation should be played at. The jumpscare has its own frame rate
    animation_frame_location = PATH + "/assets/ffaz/frames_o2" # The path to the animation frames folder. This is here because there are two versions of the animation, and I have yet to decide which one looks better.
    delay_until_song_starts = random.randint(5, 15) # wait a random number of seconds before starting the song
    time_song_plays_for = (random.randint(7, 30)*animation_frame_rate) # wait a random number of seconds before stopping the song.
    delay_until_jumpscare = random.randint(5, 24) # wait a random number of seconds before jumpscaring the player

    sleep(delay_until_song_starts/3)
    pygame.event.get() # Make Pygame do anything to keep it from being treated as "halted"
    sleep(delay_until_song_starts/3)
    pygame.event.get() # Make Pygame do anything to keep it from being treated as "halted"
    sleep(delay_until_song_starts/3)
    pygame.event.get() # Make Pygame do anything to keep it from being treated as "halted"

    pygame.mixer.Channel(0).stop()
    pygame.mixer.Channel(3).set_volume(1.0)
    pygame.mixer.Channel(3).play(pygame.mixer.Sound(PATH + '/assets/audio/music_box.wav')) # Start the music box

    looped = 0

    while looped < time_song_plays_for:
        for frame in os.listdir(animation_frame_location):
            screen.fill((0,0,0))
            if (".gif" in frame or ".png" in frame):
                surf = pygame.image.load("%s/%s"%(animation_frame_location, frame)).convert() # Loads the image
                surf.set_colorkey((0,0,0), RLEACCEL) # Configures the image to be processed at full RGB spectrum at low quality (for speed)
                rect = surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
                screen.blit(surf, rect) # Prepare the image to be shown on-screen
                pygame.event.get()

                pygame.display.flip()
                looped += 1
                clock.tick(animation_frame_rate)

    pygame.mixer.Channel(3).stop()
    screen.fill((0,0,0))
    pygame.display.flip()

    sleep(delay_until_jumpscare/3) # only wait part of the time because Windows is very harsh towards paused Pygame
    pygame.event.get() # Make Pygame do anything to keep it from being treated as "halted"
    sleep(delay_until_jumpscare/3) # only wait part of the time because Windows is very harsh towards paused Pygame
    pygame.event.get() # Make Pygame do anything to keep it from being treated as "halted"
    sleep(delay_until_jumpscare/3) # only wait part of the time because Windows is very harsh towards paused Pygame
    pygame.event.get() # Make Pygame do anything to keep it from being treated as "halted"

    # A workaround to one of the stupidest problems i've ever seen
    frameLooped = 0

    pygame.mixer.music.load(PATH + '/assets/audio/cxr_jumpscare_2.wav')
    pygame.mixer.music.play()

    while frameLooped < 24:
        for frame in os.listdir(PATH + "/assets/ffaz/frames"):
            screen.fill((0,0,0)) # Blank the screen

            if (".gif" in frame or ".png" in frame): # Make sure the file is a valid image
                surf = pygame.image.load(PATH + "/assets/ffaz/frames/%s"%frame).convert() # Loads the image
                surf.set_colorkey((0,0,0), RLEACCEL) # Configures the image to be processed at full RGB spectrum at low quality (for speed)
                rect = surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)) # Centers the image
                screen.blit(surf, rect) # Prepare the image to be shown on-screen
                pygame.event.get()

                pygame.display.flip() # Update the screen
                frameLooped += 1 # Update how many times the animation has looped
                clock.tick(60) # Limit to 60 FPS

    


class freddy(pygame.sprite.Sprite): # Same code as DJMM
    def __init__(self):
        super(freddy, self).__init__()
        self.surf = pygame.image.load(PATH + "/assets/ffaz/fred.jpeg").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(VOID, mode, screen, active_camera, location_f, location_mm):
        """ Mode can be: 'normal' (update display) or 'destroy' (get that bear outta here!) """

        if (mode == "normal") and (str(active_camera) == str(location_f)):
            surf = pygame.image.load(PATH + "/assets/ffaz/fred.jpeg").convert()
            surf.set_colorkey((255,255,255), RLEACCEL)
            rect = surf.get_rect()
            rect.center = (((SCREEN_WIDTH/2)-200, SCREEN_HEIGHT/2))

            screen.blit(surf, rect)

        else:
            NotImplemented
            # This makes the entity dissapear, since it no longer renders itself