"""Crash alerts"""

import tkinter, os
from tkinter import messagebox

def run():

    root = tkinter.Tk()
    root.iconify()
    messagebox.showwarning("Freddy's Hall", "An irrecoverable game engine crash has occured. To protect your data, Freddy's Hall has automatically closed itself.\n\nA crash report has been placed on the current user's desktop") # Show error
    root.destroy()

    os.abort()