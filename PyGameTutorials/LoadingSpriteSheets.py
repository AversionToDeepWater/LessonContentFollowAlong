import pygame
import LoadingSpriteSheetsTwo

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load(r'C:\Users\imana\PycharmProjects\LessonContentFollowAlong\AssetsPygameTut\graphics\street_animals\1 Dog\Walk.png').convert_alpha()
sprite_sheet = LoadingSpriteSheetsTwo.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50) #BG colour
black = (0,0,0)

'''
Moved to class, move to sprite sheet twoo
def get_image(sheet, frame, width, height, scale, colour):
    #first need to make a blank surface
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0),((frame * width),0, width, height)) #has taken the whole sprite sheet and only taken part of it
    #scale image and resize to make bigger
    image= pygame.transform.scale(image,(width * scale, height * scale)) #make sprite bigger or smaller
    image.set_colorkey(colour) #gets rid of black background from image and make transparent
    return image
'''
#Create animation list
animation_list= []
animation_steps = 6 #number of images in sprite sheet
last_update = pygame.time.get_ticks()
animation_cooldown = 75 #in miliseconds
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x,48,48,2,black))
    #scrpite sheet image in my case is 48x48 pixels, scaled up by 2 it's 96x96

# frame_zero = sprite_sheet.get_image(0, 48, 48,2, black) #width and height of our sprite
# frame_one = sprite_sheet.get_image( 1, 48, 48,2, black)
# frame_two = sprite_sheet.get_image( 2, 48, 48,2, black)
# frame_three = sprite_sheet.get_image(3, 48, 48,2, black)


run = True
while run:
    #update background, needs to be done before loading images ontop
    screen.fill(BG)

    #display image
    # screen.blit(sprite_sheet_image,(0,0))

    #update animation
    # if 500ms have passed between last update and current one, update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    #show frame image
    screen.blit(animation_list[frame],(0, 0))

    pygame.display.update()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

