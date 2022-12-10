try:
    import time
    from zipfile import ZipFile
    import os
    from os.path import basename

    PATH = "C:/Users/247086/Downloads/VisualStudioCode/FHALL"
    BLUE = "\u001b[34;1m" # The color blue
    YELLOW = "\u001b[33;1m" # The color yellow
    SPECIALDRIVE = "\u001b[1;38;5;120m"
    RED = "\u001b[31;1m" # The color red
    GREEN = "\u001b[32;1m"
    RESET = "\u001b[0m" # Reset to default color

    """ PACKAGE THE FILES """
    archive = ZipFile('fhall.dat', 'w')
    try:
        for folderName, subfolders, filenames in os.walk(PATH + "/assets"):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                print(YELLOW + "BUILD: " + SPECIALDRIVE + filePath + RESET)
                # Add file to zip
                archive.write(filePath, basename(filePath))

        for folderName, subfolders, filenames in os.walk(PATH + "/data"):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                print(YELLOW + "BUILD: " + SPECIALDRIVE + filePath + RESET)
                # Add file to zip
                archive.write(filePath, basename(filePath))

        for folderName, subfolders, filenames in os.walk(PATH + "/modules"):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                print(YELLOW + "BUILD: " + SPECIALDRIVE + filePath + RESET)
                # Add file to zip
                archive.write(filePath, basename(filePath))

        for folderName, subfolders, filenames in os.walk(PATH + "/scripts"):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                print(YELLOW + "BUILD: " + SPECIALDRIVE + filePath + RESET)
                # Add file to zip
                archive.write(filePath, basename(filePath))

        for folderName, subfolders, filenames in os.walk(PATH + "/settings"):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                print(YELLOW + "BUILD: " + SPECIALDRIVE + filePath + RESET)
                # Add file to zip
                archive.write(filePath, basename(filePath))
    except Exception as err:
        print(YELLOW + "BUILD:" + RED + " <ERROR> " + SPECIALDRIVE + str(err) + RESET)

    archive.write(PATH + '/core.pyw')
    print(YELLOW + "BUILD: " + SPECIALDRIVE + "core.pyw" + RESET)
    archive.write(PATH + '/config.py')
    print(YELLOW + "BUILD: " + SPECIALDRIVE + "config.py" + RESET)
    archive.write(PATH + '/fhall.ico')
    print(YELLOW + "BUILD: " + SPECIALDRIVE + "fhall.ico" + RESET)
    archive.write(PATH + '/platform')
    print(YELLOW + "BUILD: " + SPECIALDRIVE + "platform" + RESET)
    archive.write(PATH + '/uninstall.py')
    print(YELLOW + "BUILD: " + SPECIALDRIVE + "uninstall.py" + RESET)

    archive.close()
    time.sleep(15)
except Exception as err:
    print(str(err))
    time.sleep(15)