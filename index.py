import pygame # Import the Pygame module
from sys import exit # Import the "exit" function from the "sys" module

def display_score():
    global score_surface, score_rectangle, score
    total_time = pygame.time.get_ticks()
    current_time = total_time - reset_time
    score = int(current_time/100) # + more points enemy
    score_surface = test_font.render(f'Score {score}', False, 'White') #render(text, AA, color) 
    score_rectangle = score_surface.get_rect(midtop=(screen.get_width() / 2, 50))

def load():# for now use global variable
    global score_rectangle,snail_surface1, snail_rectangle, player_walk_surface_1, player_walk_rectangle_1,player_walk_surface_2, player_walk_rectangle_2, player_gravity,player_stand_surface, player_stand_rectangle, player_rotozoom, player_rotozoom_rect
    snail_surface1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha() 
    # snail_surface2 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    snail_rectangle = snail_surface1.get_rect(midbottom=(600,sky_surface.get_height()))
    player_walk_surface_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
    player_walk_rectangle_1 = player_walk_surface_1.get_rect(midbottom=(80,sky_surface.get_height()))# pygame.Rect(left,top,width,height)
    player_walk_surface_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
    player_walk_rectangle_2 = player_walk_surface_2.get_rect(midbottom=(80,sky_surface.get_height()))# pygame.Rect(left,top,width,height)

    player_gravity = 0

    player_stand_surface = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
    player_stand_rectangle = player_stand_surface.get_rect(center=(400,200))# pygame.Rect(left,top,width,height)

    player_rotozoom = pygame.transform.rotozoom(player_stand_surface,0,2) #rotozoom(Obj, deg, x zoom)
    player_rotozoom_rect= player_rotozoom.get_rect(center=(400,200))

active_jump = 2
def jump():
    global active_jump, player_gravity
    if active_jump > 0:
       player_gravity = -10
       active_jump -= 1
    

pygame.init() # Initialize the Pygame modules
reset_time = 0
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

game_start = True
game_play = False
game_pause = False
game_over = False

def check_game_status():
    global game_start, game_play, game_pause, game_over
    print("game_start : ", game_start)
    print("game_play : ", game_play)
    print("game_pause : ", game_pause)
    print("game_over : ", game_over) 
    return   
           
# load static image
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Ottieni il nome del controller e il numero di assi e bottoni
game_name = test_font.render('Pixel Runner',False,"black")
game_name_rect = game_name.get_rect(center =(400,130))
# Set the player's movement speed
player_speed = 600
# State variable to track the direction of movement
move_direction = 0
# Set a fixed time interval to refresh character position
move_interval = 10 # in milliseconds
move_timer = pygame.time.get_ticks() + move_interval

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

# controller joystick
def controller_btn_case(i):
    global player_gravity, game_pause, game_play, game_start,game_over, reset_time
    if i == 0:
        print("Hai premuto il pulsante A") 
        if game_play:
            jump()           
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
        print("Hai premuto il pulsante START del controller")
        if game_start: 
            game_start = False
            game_play = True
            reset_time = pygame.time.get_ticks()
        elif game_over: 
            game_over = False
            game_start = True
        elif game_pause: 
            game_pause = False
            game_play = True
        elif game_play: 
            game_pause = True
            game_play = False
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

        # if event.type == pygame.MOUSEBUTTONUP:
        #     print('mouse up')
        # if event.type == pygame.KEYUP:
        #     print('keyup')

        if event.type == pygame.JOYBUTTONDOWN:               
            for i in range(joystick.get_numbuttons()):
                if joystick.get_button(i):
                    print(f"Pulsante {i} premuto")          
                    controller_btn_case(i)

        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 5:  # RT
                rt_value = joystick.get_axis(5)
                print("RT value:", rt_value)
            if event.axis == 4:  # LT
                lt_value = joystick.get_axis(4)
                print("LT value:", lt_value)

            if event.axis == 3:  # analogic DX axis Y -3.0517578125e-05 if 0
                right_stick_y_value = joystick.get_axis(3) 
                print("right_stick_y_value:", right_stick_y_value) # -1=🠕 ~ 1=🠗 
            if event.axis == 2:  # analogic DX axis X 0 if 0
                right_stick_x_value = joystick.get_axis(2)
                print("right_stick_x_value:", right_stick_x_value) # -1=🠔 ~ 1=🠖

            if event.axis == 1:  # analogic DX axis Y -3.0517578125e-05 if 0
                left_stick_y_value = joystick.get_axis(1) 
                print("left_stick_y_value:", left_stick_y_value) # -1=🠕 ~ 1=🠗 
            if event.axis == 0:  # analogic DX axis X 0 if 0
                left_stick_x_value = joystick.get_axis(0)
                print("left_stick_x_value:", left_stick_x_value) # -1=🠔 ~ 1=🠖
                if left_stick_x_value > 0.5:
                    move_direction = 1
                elif left_stick_x_value < -0.5:
                    move_direction = -1
                else:
                    move_direction = 0
                
        
        
        if game_play:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_walk_rectangle_1.collidepoint(event.pos): 
                    player_gravity = -10 

            if event.type == pygame.MOUSEMOTION:
                if player_walk_rectangle_1.collidepoint(event.pos): 
                    print('collision')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_pause = False

        elif game_pause:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_pause = False
                if event.key == pygame.K_RETURN:
                    print("invio")

        elif game_over or game_start: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("invio")
                    reset_time = pygame.time.get_ticks()
                    if game_start:
                        print("miao")
                        game_start = False
                    else: 
                        game_start = True
                        game_over = False
                    
                    
                   
                    
            
       
        
       
    if game_start:
        load()
        screen.fill((94,129,162))
        screen.blit(player_rotozoom,player_rotozoom_rect)
        # if 'score' in globals():
        if 'score' in locals():
            score_message = test_font.render(f'Your score: {score}', False, (111,196,169))
            score_message_rect = score_message.get_rect(center=(400,330))
            screen.blit(score_message, score_message_rect)
        else:
            game_message = test_font.render('Press start to play', False, (111,196,169))
            game_message_rect = game_message.get_rect(center=(400,330))
            screen.blit(game_message, game_message_rect)
       
    if game_play:
        # draw image background
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,sky_surface.get_height()))

        # score
        display_score()
        pygame.draw.rect(screen, '#c0e8ec', score_rectangle.inflate(20, 10), 100)  # outer rectangle
        screen.blit(score_surface,score_rectangle)

        # snail
        snail_rectangle.x -= 8
        if snail_rectangle.right <= 0 : snail_rectangle.left = 800 
        screen.blit(snail_surface1, snail_rectangle)

        # player
        # Refresh character position based on fixed time interval
        if pygame.time.get_ticks() >= move_timer:
            player_walk_rectangle_1.x += move_direction * player_speed * move_interval / 1000
            move_timer = pygame.time.get_ticks() + move_interval

        #Gravity
        player_gravity += 0.5
        player_walk_rectangle_1.y += player_gravity
        if player_walk_rectangle_1.bottom >= 300: 
            player_walk_rectangle_1.bottom = 300 
            active_jump = 2  
        screen.blit(player_walk_surface_1, player_walk_rectangle_1)

        #collision
        if player_walk_rectangle_1.colliderect(snail_rectangle): 
            game_over = True
            game_play = False
            
     
    elif game_over:
        game_over_surface = test_font.render('Game Over', False, 'Black') #render(text, AA, color)
        game_over_rectangle = game_over_surface.get_rect(midtop=(screen.get_width() / 2, 50))
        pygame.draw.rect(screen, 'Red', game_over_rectangle.inflate(20, 10), 100)  # outer rectangle
        screen.blit(game_over_surface,game_over_rectangle)

        restart_surface = test_font.render('Restart', False, 'Gold') #render(text, AA, color)
        restart_rectangle = restart_surface.get_rect(midtop=(screen.get_width() / 2, 250))
        pygame.draw.rect(screen, 'Red', restart_rectangle.inflate(50, 40), 100)  # outer rectangle
        screen.blit(restart_surface,restart_rectangle)
           
    elif game_pause:
        score_surface = test_font.render('Pause', False, 'Black') #render(text, AA, color)
        score_rectangle = score_surface.get_rect(midtop=(screen.get_width() / 2, 50))
        pygame.draw.rect(screen, 'Green', score_rectangle.inflate(50, 30), 100)  # outer rectangle
        screen.blit(score_surface,score_rectangle)


    # Update the game's graphics and display them on the screen
    pygame.display.update()
    clock.tick(60)


