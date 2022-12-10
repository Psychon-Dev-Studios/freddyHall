def dumpDebugDataUponImportCrash(crashCause):
    import tkinter, os
    from tkinter import messagebox
    from modules.constants import WINDRIVE
    from time import localtime as tm
    userDesktop = "%s:/Users/%s/Desktop/"%(WINDRIVE, os.getlogin())
    currentTime = str(tm()[1]) + "/" + str(tm()[2]) + "/" + str(tm()[0]) + ", " + str(tm()[3]) + ":" + str(tm()[4]) # Get the current time

    try:
        file = open(userDesktop + "/fh_fatalErrorReport.log", "x")
        file.write("Fatal Crash at %s. FH_debugger reported: %s\n"%(currentTime, crashCause))
        file.close()

    except:
        file = open(userDesktop + "/fh_fatalErrorReport.log", "a")
        file.write("Fatal Crash at %s. FH_debugger reported: %s\n"%(currentTime, crashCause))
        file.close()