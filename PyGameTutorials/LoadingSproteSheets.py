import pygame

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load(r'C:\Users\imana\PycharmProjects\LessonContentFollowAlong\AssetsPygameTut\graphics\street_animals\1 Dog\Walk.png').convert_alpha()
BG = (50, 50, 50) #BG colour

def get_image(sheet, width, height, scale):
    #first need to make a blank surface
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0),(0,0, width, height)) #has taken the whole sprite sheet and only taken part of it
    #scale image and resize to make bigger
    image= pygame.transform.scale(image,(width * scale, height * scale))
    return image

frame_zero = get_image(sprite_sheet_image, 48, 48,2) #width and height of our sprite

run = True
while run:
    #update background, needs to be done before loading images ontop
    screen.fill(BG)

    #display image
    # screen.blit(sprite_sheet_image,(0,0))
    screen.blit(frame_zero, (0,0))

    pygame.display.update()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

