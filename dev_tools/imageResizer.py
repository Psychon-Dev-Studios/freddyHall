import os
from PIL import Image

PATH  = "C:/Users/247086/Desktop/AP CSP Final Project/assets/ffaz/frames_demonic"
ARATIO = (1920, 1080)
sinImageName = "office_door.png"

# Frame resizer
for frame in os.listdir(PATH):
    image = Image.open(PATH + "/" + frame)
    print("Opening %s" %frame)

    Image.Image.resize(image, ARATIO).save(PATH + "/" + frame)

    print("Saving %s" %frame)

print("Done")

# Single image resizer
"""
image = Image.open(PATH + "/" + sinImageName)
print("Opening %s"%(PATH+"/"+sinImageName))
Image.Image.resize(image, ARATIO).save(PATH + "/" + sinImageName)
print("Saving %s"%(PATH+"/"+sinImageName))
"""