import pygame # Import the Pygame module
from sys import exit # Import the "exit" function from the "sys" module

pygame.init() # Initialize the Pygame modules

# Create a game window with width 900 and height 500 and store it in a variable called "screen"
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('RunnerJump') # set title 
programIcon = pygame.image.load('graphics/Player/jump.png') 
pygame.display.set_icon(programIcon) # it looks bad because you have to use a 32x32
test_font = pygame.font.Font('font/Pixeltype.ttf' , 50)

# Create a Pygame clock object that will be used to regulate the game's frame rate
clock = pygame.time.Clock()

# load image
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black') #render(text, AA, color)

snail_surface1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_surface2 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface1.get_rect(midbottom=(600,sky_surface.get_height()))
snail_x_pos = 600

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# pygame.Rect(left,top,width,height)
player_rectangle = player_surface.get_rect(midbottom=(80,sky_surface.get_height()))
# Start an infinite loop that will keep the game running until the user closes the window
while True:
    for event in pygame.event.get(): # Check for any events in the event queue
        if event.type == pygame.QUIT: # If the user closes the window
            pygame.quit() # Close Pygame and exit the program
            exit()  # Exit the program
    # draw image
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,sky_surface.get_height()))
    screen.blit(text_surface,(350,50))
    snail_rectangle.x -= 4
    if snail_rectangle.right == 0 : snail_rectangle.left = 800 
    screen.blit(snail_surface1, snail_rectangle)
    screen.blit(player_surface, player_rectangle)

    print(player_rectangle.colliderect(snail_rectangle))


    # Update the game's graphics and display them on the screen
    pygame.display.update()
    clock.tick(60)