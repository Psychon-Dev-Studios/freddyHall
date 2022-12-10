"""Enables the program to log various messages, such as crashes, internal errors, or warnings"""

import os, subprocess, sys
from threading import Thread as thread
from scripts import alert_upon_crash
from modules.fakes import *
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
spec = spec_from_loader("settings", SourceFileLoader("settings", sys.path[0] + "/settings/game.conf"))
sets = module_from_spec(spec)
spec.loader.exec_module(sets)
sys.modules['config'] = sets

from config import *

class manifest():
    appName = "Freddy's Hall"
    appID = u"csp.fh"
    appVersion = "1.0.0_framework"
    channel = "CSP.development"
    author = "Alexandra B. & Xander E-P"

def throwCrashAlert():
    alert_upon_crash.run()

# Game crash handling
def log_crash(reason,resolution):
    """Log the game crash"""
    from time import localtime as tm

    # Create a crash log on the user's desktop

    uuid = os.getlogin() # Get the current user's login, used to find their desktop location
    currentTime = str(tm()[1]) + "/" + str(tm()[2]) + "/" + str(tm()[0]) + ", " + str(tm()[3]) + ":" + str(tm()[4]) # Get the current time

    try:
        open("C:/Users/" + uuid + "/Desktop/CRASH_REPORT.log", "x").close() # Try to create a new crash report
        file = open("C:/Users/" + uuid + "/Desktop/CRASH_REPORT.log", "a") # Append mode

        file.write(manifest.appName + " detected a crash: " + currentTime + " Cause: \"" + reason + "\" Screen resolution: \"%s\"\n" %(resolution)) # Write what happened to the crash report
        file.close()
    except:
        file = open("C:/Users/" + uuid + "/Desktop/CRASH_REPORT.log", "a") # Open the crash report in append mode

        file.write(manifest.appName + " detected a crash: " + currentTime + " Cause: \"" + reason + "\" Screen resolution: \"%s\"\n" %(resolution)) # Write what happened to the crash report
        file.close()

    if (KIOSK_MODE == True):
        subprocess.run("explorer.exe")

    # Create the crash message in a seperate thread of control
    thread(name="crash_alert", target=throwCrashAlert).start()