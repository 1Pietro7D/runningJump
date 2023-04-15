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
name = joystick.get_name()
axes = joystick.get_numaxes()
buttons = joystick.get_numbuttons()
print(f"Controller connesso: {name}")
print(f"Assi: {axes}")
print(f"Bottoni: {buttons}")

# Create a Pygame clock object that will be used to regulate the game's frame rate
clock = pygame.time.Clock()

game_active = True
game_over = False

# load image
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = test_font.render('My game', False, 'White') #render(text, AA, color) 
score_rectangle = score_surface.get_rect(midtop=(screen.get_width() / 2, 50))

snail_surface1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_surface2 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface1.get_rect(midbottom=(600,sky_surface.get_height()))
player_gravity = 0
# Ottieni il nome del controller e il numero di assi e bottoni




player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# pygame.Rect(left,top,width,height)
player_rectangle = player_surface.get_rect(midbottom=(80,sky_surface.get_height()))

# controller joystick
def controller_btn_case(i): # DON'T find LT and RT
    global player_gravity
    global game_active
    if i == 0:
        player_gravity = -10
        print("Hai premuto il pulsante A") 
    elif i == 1:
        print("Hai premuto il pulsante B")
    elif i == 2:
        print("Hai premuto il pulsante X del controller")
    elif i == 3:
        print("Hai premuto il pulsante Y del controller")
    elif i == 4:
        print("Hai premuto il pulsante LB del controller")
    elif i == 5:
        print("Hai premuto il pulsante RB del controller")
    elif i == 6:
        print("Hai premuto il pulsante SELECT del controller")
    elif i == 7:
        if game_active: game_active = False
        else: game_active = True
        print("Hai premuto il pulsante START del controller")
    elif i == 8:
        print("Hai premuto il pulsante ANALOGICO SX del controller")
    elif i == 9:
        print("Hai premuto il pulsante ANALOGICO DX del controller")
    elif i == 10: # don't work because I've Xbox, and open it
        print("Hai premuto il pulsante Home del controller")

# Start an infinite loop that will keep the game running until the user closes the window
while True:
    for event in pygame.event.get(): # Check for any events in the event queue
        if event.type == pygame.QUIT: # If the user closes the window
            pygame.quit() # Close Pygame and exit the program
            exit()  # Exit the program

        if event.type == pygame.MOUSEBUTTONUP:
            print('mouse up')
        if event.type == pygame.KEYUP:
            print('keyup')

        if event.type == pygame.JOYBUTTONDOWN:               
            for i in range(joystick.get_numbuttons()):
                if joystick.get_button(i):
                    print(f"Pulsante {i} premuto")          
                    controller_btn_case(i)

        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos): 
                    player_gravity = -10 

            if event.type == pygame.MOUSEMOTION:
                if player_rectangle.collidepoint(event.pos): 
                    print('collision')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = False
        elif not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
            
        
        
       
    
    if game_active:
        # draw image background
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,sky_surface.get_height()))

        # score
        pygame.draw.rect(screen, '#c0e8ec', score_rectangle.inflate(20, 10), 100)  # outer rectangle
        screen.blit(score_surface,score_rectangle)

        # snail
        # snail_rectangle.x -= 4
        # if snail_rectangle.right == 0 : snail_rectangle.left = 800 
        # screen.blit(snail_surface1, snail_rectangle)

        # player
        player_gravity += 0.5
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300   
        screen.blit(player_surface, player_rectangle)

        #collision
        if player_rectangle.colliderect(snail_rectangle): 
            game_active = False
            game_over = True

    elif game_over:
        score_surface = test_font.render('Game Over', False, 'Black') #render(text, AA, color)
        score_rectangle = score_surface.get_rect(midtop=(screen.get_width() / 2, 50))
        pygame.draw.rect(screen, 'Red', score_rectangle.inflate(20, 10), 100)  # outer rectangle
        screen.blit(score_surface,score_rectangle)


    # Update the game's graphics and display them on the screen
    pygame.display.update()
    clock.tick(60)


