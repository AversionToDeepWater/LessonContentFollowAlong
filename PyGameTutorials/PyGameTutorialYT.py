import pygame
from sys import exit #closes any time of code once you call it, more secure way to stop while loop

#have to call this once, and it initialises everything
pygame.init() #starts pygame and initials all the parts needed fot it to run such as images and sounds

#CREATING DISPLAY SURFACE
#shows screen for a very short time, therefore need to use while true loop
screen = pygame.display.set_mode((800,400)) #width, height
pygame.display.set_caption('DOGTECTIVE') #the title of our game!

#controlling frame rate - saying the min and max frame rate
clock = pygame.time.Clock()

#MAKING SURFACES
#Plain surface!
#will need a tuple with width and height of surface, similar to screen
test_surface = pygame.Surface((100,200))
test_surface.fill('Red')  #fill our surface, there is a list of colours you can use on pygame website


#MAKING EVENT LOOP
while True:
    # draw all our elements

    for event in pygame.event.get(): #gets us all the events
        if event.type == pygame.QUIT: #i.e closing window
            pygame.quit() #this is the opposite of pygame.init()
            exit() #this will stop the code running, more secure than break for while loop - import from sys
    screen.blit(test_surface,(200,100))
    # update everything and display surface
    pygame.display.update() # only have to call it once, like pygame.init()
    clock.tick(60) #saying game should not run faster than 60fps - need to make sure game is not too complex