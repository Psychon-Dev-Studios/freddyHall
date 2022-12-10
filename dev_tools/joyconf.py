import pygame, time
from threading import Thread as td

BLUE = "\u001b[34;1m" # The color blue
YELLOW = "\u001b[33;1m" # The color yellow
RED = "\u001b[31;1m" # The color red
GREEN = "\u001b[32;1m"
RESET = "\u001b[0m" # Reset to default color

# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
joy_ID = 0
print("Python Controller configuration utitility. Use to determine controller layouts for unusual / partially supported controllers")
print("Make sure your controller is configured correctly to use joystick 1, or change joy_ID to your joystick ID.")
print(BLUE + "Type in a number and press enter to change controller ID" + RESET)

def joyID_change():
    global joystick, joy_ID
    while True:
        try:
            newJoyID = int(input(""))

            try:
                joystick = pygame.joystick.Joystick(newJoyID)
                joy_ID = newJoyID
            except:print(RED + "No controller with ID %s found; ID not changed"%newJoyID + RESET)

        except:print(RED + "New joystick ID be a whole number" + RESET)

pygame.init()
screen = pygame.display.set_mode((400, 40))

pygame.display.set_caption("Python Controller Configuration")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

if (pygame.joystick.get_count() != 0):
    try:joystick = pygame.joystick.Joystick(joy_ID)
    except:joystick = None;print(RED + "No controller connected" + RESET)
else:joystick=None;print(RED + "No controller connected" + RESET)
# Get ready to print.
if joystick != None:
    counterDisplay = pygame.font.Font("C:/users/247086/downloads/fonts/fps.ttf", 16).render(pygame.joystick.Joystick(joy_ID).get_name(), True, (155,255,155))
    counterBox = counterDisplay.get_rect()
    counterBox.center = (200,20)
    screen.blit(counterDisplay, counterBox)
    pygame.display.update()
else:
    counterDisplay = pygame.font.Font("C:/users/247086/downloads/fonts/fps.ttf", 16).render("Disconnected", True, (255,155,155))
    counterBox = counterDisplay.get_rect()
    counterBox.center = (200,20)
    screen.blit(counterDisplay, counterBox)
    pygame.display.update()

td(name="inputThread", target=joyID_change).start()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            try:
                if(joystick.get_button(0)):print("depress 0")
            except:NotImplemented
            try:
                if(joystick.get_button(1)):print("depress 1")
            except:NotImplemented
            try:
                if(joystick.get_button(2)):print("depress 2")
            except:NotImplemented
            try:
                if(joystick.get_button(3)):print("depress 3")
            except:NotImplemented
            try:
                if(joystick.get_button(4)):print("depress 4")
            except:NotImplemented
            try:
                if(joystick.get_button(5)):print("depress 5")
            except:NotImplemented
            try:
                if(joystick.get_button(6)):print("depress 6")
            except:NotImplemented
            try:
                if(joystick.get_button(7)):print("depress 7")
            except:NotImplemented
            try:
                if(joystick.get_button(8)):print("depress 8")
            except:NotImplemented
            try:
                if(joystick.get_button(9)):print("depress 9")
            except:NotImplemented
            try:
                if(joystick.get_button(10)):print("depress 10")
            except:NotImplemented
            try:
                if(joystick.get_button(11)):print("depress 11")
            except:NotImplemented
            try:
                if(joystick.get_button(12)):print("depress 12")
            except:NotImplemented
            try:
                if(joystick.get_button(13)):print("depress 13")
            except:NotImplemented
            try:
                if(joystick.get_button(14)):print("depress 14")
            except:NotImplemented

        elif event.type == pygame.JOYAXISMOTION:
            try:
                if(joystick.get_axis(0)>0.4 or joystick.get_axis(0)<-0.4):print("move 0 at %s"%joystick.get_axis(0))
            except:NotImplemented
            try:
                if(joystick.get_axis(1)>0.4 or joystick.get_axis(1)<-0.4):print("move 1 at %s"%joystick.get_axis(1))
            except:NotImplemented
            try:
                if(joystick.get_axis(2)>0.4 or joystick.get_axis(2)<-0.4):print("move 2 at %s"%joystick.get_axis(2))
            except:NotImplemented
            try:
                if(joystick.get_axis(3)>0.4 or joystick.get_axis(3)<-0.4):print("move 3 at %s"%joystick.get_axis(3))
            except:NotImplemented
            try:
                if(joystick.get_axis(4)>0.4 or joystick.get_axis(4)<-0.4):print("move 4 at %s"%joystick.get_axis(4))
            except:NotImplemented
            try:
                if(joystick.get_axis(5)>0.4 or joystick.get_axis(5)<-0.4):print("move 5 at %s"%joystick.get_axis(5))
            except:NotImplemented
            try:
                if(joystick.get_axis(6)>0.4 or joystick.get_axis(6)<-0.4):print("move 6 at %s"%joystick.get_axis(6))
            except:NotImplemented
            try:
                if(joystick.get_axis(7)>0.4 or joystick.get_axis(7)<-0.4):print("move 7 at %s"%joystick.get_axis(7))
            except:NotImplemented
            try:
                if(joystick.get_axis(8)>0.4 or joystick.get_axis(8)<-0.4):print("move 8 at %s"%joystick.get_axis(8))
            except:NotImplemented
            try:
                if(joystick.get_axis(9)>0.4 or joystick.get_axis(9)<-0.4):print("move 9 at %s"%joystick.get_axis(9))
            except:NotImplemented

        elif event.type == pygame.JOYDEVICEREMOVED:
            screen.fill((0,0,0))
            counterDisplay = pygame.font.Font("C:/users/247086/downloads/fonts/fps.ttf", 16).render("Disconnected", True, (255,155,155))
            counterBox = counterDisplay.get_rect()
            counterBox.center = (200,20)
            screen.blit(counterDisplay, counterBox)
            pygame.display.update()
            print(RED + "Controller disconnected" + RESET)

        elif event.type == pygame.JOYDEVICEADDED:
            print(GREEN + "Controller connected! " + YELLOW + pygame.joystick.Joystick(joy_ID).get_name() + GREEN + ", %s total joysticks, Joystick ID %s"%(pygame.joystick.get_count(),joy_ID)+RESET)
            print(GREEN + "Rumbling " + YELLOW + pygame.joystick.Joystick(joy_ID).get_name() + GREEN + " for 5 seconds" + RESET)
            try:joystick.rumble(0, 5000, 1000) # Rumble
            except:print(RED + "Rumble failed" + RESET)

        try:
            screen.fill((0,0,0))
            joystick = pygame.joystick.Joystick(joy_ID)
            counterDisplay = pygame.font.Font("C:/users/247086/downloads/fonts/fps.ttf", 16).render(pygame.joystick.Joystick(joy_ID).get_name(), True, (155,255,155))
            counterBox = counterDisplay.get_rect()
            counterBox.center = (200,20)
            screen.blit(counterDisplay, counterBox)
        except:
            screen.fill((0,0,0))
            counterDisplay = pygame.font.Font("C:/users/247086/downloads/fonts/fps.ttf", 16).render("Disconnected", True, (255,155,155))
            counterBox = counterDisplay.get_rect()
            counterBox.center = (200,20)
            screen.blit(counterDisplay, counterBox)
        
        pygame.display.update()
pygame.quit()