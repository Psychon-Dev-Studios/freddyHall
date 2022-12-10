""" Connection monitoring tests. These are only used if the player is clientConnected """

from modules.djmm import PATH
import time as systime, pygame
from pygame import *

from modules.constants import SCREEN_HEIGHT, SCREEN_WIDTH

def test_connection():
    try:
        timeSinceLastUpdate = float(open(PATH + "/data/pingTime").read())
    except:
        timeSinceLastUpdate = -0.1
    now = systime.time()

    try:
        difference = now-timeSinceLastUpdate
    except:
        difference = 500

    return difference

def draw_stat_text(font, screen, frames):
    if (frames % 10 == 0):
        difference = test_connection()
        file = open(PATH + "/data/ping_cache", "w")
        file.write(str(difference))
        file.close()
    else:
        difference = float(open(PATH + "/data/ping_cache").read())
    
    if  (difference < 0.9):color = (0, 255, 64)
    elif (difference > 0.9 and difference < 2.5):color = (224, 253, 78)
    elif (difference > 2.5 and difference < 3.5):color = (255, 174, 0)
    elif (difference > 3.5 and difference < 60):color = (255, 77, 0)
    elif (difference > 60):color = (50,50,50)
    else:color= (194, 194, 194)

    statDisplay = font.render(str(round(difference*1000)) + "ms/" + str(round(difference)) + "sec", True, color)
    statBox = statDisplay.get_rect()
    statBox.topleft = (40, SCREEN_HEIGHT - 20)
    screen.blit(statDisplay, statBox)