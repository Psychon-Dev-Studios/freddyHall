""" Makes my life a lot easier """
import os # Shuddup error

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080 # Screen dimensions
FRAME_RATE = 24 # In-game frame rate. Does not effect the frame rate of animations like jumpscares.
HOUR_LENGTH = 60 # How long, in seconds, each hour should be
WINDRIVE = str(os.environ['WINDIR'].split(":\\")[0])

class manifest():
    """ The power of MANIFEST compells you """
    appName = "Freddy's Hall"
    appID = u"freehall"
    appVersion = "1.2.0"
    channel = "beta"
    author = "Princess & Kytten"