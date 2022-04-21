"""Verifies various important information, such as if dependencies are available"""
import os, subprocess, tkinter, sys
from tkinter import messagebox
PATH = sys.path[0]

def verify_dependencies():
    """Attempts to determine if any required modules are missing"""
    
    missing_dependencies = []

    try:
        import pygame
    except:
        missing_dependencies.append("pygame")

    try:
        import pygame_widgets
    except:
        missing_dependencies.append("pgw")


    if (len(missing_dependencies) > 0):
        
        root = tkinter.Tk()
        root.iconify()
        installRequired = messagebox.askokcancel("Missing or Damaged Dependencies", "This program cannot be started because a required module is missing. Click OK to install the required modules, or Cancel to abort") # Show error
        root.destroy()

        if (installRequired == True):
            install_dependencies()
        else:
            os.abort()

def install_dependencies():
    """Attempt to install missing dependencies"""

    try:
        subprocess.call("pip install pygame") # Attempt to install pygame
        subprocess.call("pip install pygame_widgets")
    except Exception as err:
        root = tkinter.Tk()
        root.iconify()
        keep_going = messagebox.askyesno("Install Failed", "Installation of a required module failed. Based on the following message, should we proceed anyways? Message: " + str(err)) # Show error
        root.destroy()

        if (keep_going == False):
            os.abort()

    try:
        import pygame, pygame_widgets
        
    except Exception as err:
        root = tkinter.Tk()
        root.iconify()
        keep_going = messagebox.askyesno("Install Failed", "Initialization of a required module failed (likely due to a failed install). Based on the following message, should we proceed anyways? Message: " + str(err)) # Show error
        root.destroy()

        if (keep_going == False):
            os.abort()