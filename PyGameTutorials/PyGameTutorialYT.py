import pygame
from sys import exit #closes any time of code once you call it, more secure way to stop while loop

#have to call this once, and it initialises everything
pygame.init() #starts pygame and initials all the parts needed fot it to run such as images and sounds

#CREATING DISPLAY SURFACE
#shows screen for a very short time, therefore need to use while true loop
screen = pygame.display.set_mode((640,384)) #width, height
pygame.display.set_caption('DOGTECTIVE') #the title of our game!

#controlling frame rate - saying the min and max frame rate
clock = pygame.time.Clock()

#FONT
test_font = pygame.font.Font(None, 50) #None gives you the default pygame font

#MAKING SURFACES
#Plain surface!
#will need a tuple with width and height of surface, similar to screen
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')  #fill our surface, there is a list of colours you can use on pygame website

#Using background hills assets
sky_surface = pygame.image.load(r'C:\Users\imana\PycharmProjects\LessonContentFollowAlong\AssetsPygameTut\graphics\background_hills\background1.png').convert()
foreground_surface = pygame.image.load(r'C:\Users\imana\PycharmProjects\LessonContentFollowAlong\AssetsPygameTut\graphics\background_hills\background2.png').convert()
trees_surface = pygame.image.load(r'C:\Users\imana\PycharmProjects\LessonContentFollowAlong\AssetsPygameTut\graphics\background_hills\background3.png').convert()
floor_surface = pygame.image.load(r'C:\Users\imana\PycharmProjects\LessonContentFollowAlong\AssetsPygameTut\graphics\background_hills\background4.png').convert()

#text surface
text_surface = test_font.render("Dogtective", False, 'Black')

#dog
dog_surface = pygame.image.load(r'C:\Users\imana\PycharmProjects\LessonContentFollowAlong\AssetsPygameTut\graphics\street_animals\1 Dog\Idle.png').convert_alpha()

#MAKING EVENT LOOP
while True:
    # draw all our elements

    for event in pygame.event.get(): #gets us all the events
        if event.type == pygame.QUIT: #i.e closing window
            pygame.quit() #this is the opposite of pygame.init()
            exit() #this will stop the code running, more secure than break for while loop - import from sys
    screen.blit(sky_surface,(0,0))
    screen.blit(foreground_surface,(0,30))
    screen.blit(trees_surface,(0,40))
    screen.blit(floor_surface,(0,55))
    # screen.blit(text_surface,(200,50))
    # screen.blit(dog_surface,(100,50))
    # update everything and display surface
    pygame.display.update() # only have to call it once, like pygame.init()
    clock.tick(60) #saying game should not run faster than 60fps - need to make sure game is not too complex