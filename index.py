import pygame # Import the Pygame module
from sys import exit # Import the "exit" function from the "sys" module

pygame.init() # Initialize the Pygame modules

# Create a game window with width 900 and height 500 and store it in a variable called "screen"
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('RunnerJump') # set title 
programIcon = pygame.image.load('graphics/Player/jump.png') 
pygame.display.set_icon(programIcon) # it looks bad because you have to use a 32x32
test_font = pygame.font.Font('font/Pixeltype.ttf' , 50)

joystick_count = pygame.joystick.get_count() # Create a joystick object for the first joystick
joystick = pygame.joystick.Joystick(0) # Create a joystick object for the first joystick
joystick.init() # Initialize the joystick

# Create a Pygame clock object that will be used to regulate the game's frame rate
clock = pygame.time.Clock()

# load image
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
score_surface = test_font.render('My game', False, 'White') #render(text, AA, color)
score_rectangle = score_surface.get_rect(midtop=(screen.get_width() / 2, 50))
snail_surface1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_surface2 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface1.get_rect(midbottom=(600,sky_surface.get_height()))
player_gravity = 0

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# pygame.Rect(left,top,width,height)
player_rectangle = player_surface.get_rect(midbottom=(80,sky_surface.get_height()))
# Start an infinite loop that will keep the game running until the user closes the window
while True:
    for event in pygame.event.get(): # Check for any events in the event queue
        if event.type == pygame.QUIT: # If the user closes the window
            pygame.quit() # Close Pygame and exit the program
            exit()  # Exit the program

        if event.type == pygame.MOUSEBUTTONUP:
            print('mouse up')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos): 
                player_gravity = -20

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == joystick.get_button(1):  # 0 is the button A/B of controller, 1 is A or B 
                player_gravity = -20
            if event.button == pygame.CONTROLLER_BUTTON_A:
                print("Hai premuto il pulsante A del controller")

        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos): 
                print('collision')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
                print('jump')

        if event.type == pygame.KEYUP:
            print('keyup')
        
       
    

    # draw image background
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,sky_surface.get_height()))

    # score
    pygame.draw.rect(screen, '#c0e8ec', score_rectangle.inflate(20, 10), 100)  # outer rectangle
    screen.blit(score_surface,score_rectangle)
    
    # snail
    snail_rectangle.x -= 4
    if snail_rectangle.right == 0 : snail_rectangle.left = 800 
    screen.blit(snail_surface1, snail_rectangle)

    # player
    player_gravity += 1
    player_rectangle.y += player_gravity
    if player_rectangle.bottom >= 300: player_rectangle.bottom = 300   
    screen.blit(player_surface, player_rectangle)
    
    #collision
    if player_rectangle.colliderect(snail_rectangle): 
        pygame.quit()
        exit()

    # Update the game's graphics and display them on the screen
    pygame.display.update()
    clock.tick(60)