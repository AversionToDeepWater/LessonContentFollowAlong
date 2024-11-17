import pygame
from sys import exit #closes any time of code once you call it, more secure way to stop while loop

#have to call this once, and it initialises everything
pygame.init() #starts pygame and initials all the parts needed fot it to run such as images and sounds

#CREATING DISPLAY SURFACE
#shows screen for a very short time, therefore need to use while true loop
screen = pygame.display.set_mode((800,400)) #width, height
pygame.display.set_caption('DOGTECTIVE') #the title of our game!

while True:
    #MAKING EVENT LOOP
    # draw all our elements
    # update everything and display surface
    for event in pygame.event.get(): #gets us all the events
        if event.type == pygame.QUIT: #i.e closing window
            pygame.quit() #this is the opposite of pygame.init()
            exit() #this will stop the code running, more secure than break for while loop

    pygame.display.update() # only have to call it once, like pygame.init()