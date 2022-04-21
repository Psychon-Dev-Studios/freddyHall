import os, shutil, time
print("Don't close this terminal, we're uninstalling Freddy's Hall")
remErrors=0

time.sleep(5)

WINDRIVE = str(os.environ['WINDIR'].split(":\\")[0])
USER = os.getlogin()
DP = WINDRIVE + ":/ProgramData/fhall/"

os.system("title Uninstalling")

print("Attempting to remove game files")
def REM():
    global remErrors
    try:
        shutil.rmtree(DP)
    except:
        remErrors += 1
        print("Attempt %s failed"%remErrors)
        time.sleep(2)
        if remErrors > 8:
            print("Abort")
            os.abort()
        else:
            REM()

REM()

try:
    os.remove("%s:/Users/%s/Desktop/Freddy's Hall.lnk"%(WINDRIVE, USER))
    os.remove("%s:/Users/%s/Desktop/FLink.lnk"%(WINDRIVE, USER))
except:
    print("Removal of shortcuts failed. You may have to manually remove them")

time.sleep(5)
os.abort()