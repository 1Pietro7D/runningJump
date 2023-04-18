import pygame # Import the Pygame module
from sys import exit # Import the "exit" function from the "sys" module
from random import randint

ground = 300
reset_time = 0
def display_score():
    global score_surface, score_rectangle, score, pause_time_list
    total_time = pygame.time.get_ticks()
    current_time = total_time - reset_time
    score = int((current_time - (sum(pause_time_list))) /100) # + more points enemy
    score_surface = test_font.render(f'Score {score}', False, 'White') #render(text, AA, color) 
    score_rectangle = score_surface.get_rect(midtop=(screen.get_width() / 2, 50))

### DRAW OBSTACLE ###
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            ## DRAW SNAIL and FLY
            if obstacle_rect.bottom == ground:  
                screen.blit(animation(snail), obstacle_rect)
            if obstacle_rect.bottom == 150:
                screen.blit(animation(fly), obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > -100 ]
        return obstacle_list
    else: return []

def animation(obstacle_surf):
    global obstacle_index
    obstacle_index += 0.05
    if obstacle_index >= len(obstacle_surf): 
        obstacle_index = 0
    
    return obstacle_surf[int(obstacle_index)]


### PLAYER ANIMATION ###
def player_animation():
    global player_index, player_surf
    # player walking animation if the player is on floor
    if player_rect.bottom < ground:
        player_index = 2
        player_surf = player_run[player_index]
    else:
        player_index += 0.1
        if player_index >= len(player_run) - 1: 
            player_index = 0
        player_surf = player_run[int(player_index)]

    # display the jump surface when player is not on floor

def load():# for now use global variable
    global fly, snail, obstacle_index, player_run, player_index, player_surf, player_rect, player_gravity, obstacle_rect_list, pause_time, resume_time, pause_time_list

    ### Obstacle ###
    ## Snail ##
    snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha() 
    snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
    snail = [snail_1,snail_2]

    ## Fly ##
    fly_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha() 
    fly_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
    fly = [fly_1, fly_2]

    obstacle_index = 0
    obstacle_rect_list = []

    pause_time = 0
    resume_time = 0
    pause_time_list = []


    player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha() 
    player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
    player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
    player_run = [player_walk_1, player_walk_2, player_jump]
    player_index = 0

    player_surf = player_run[player_index]
    player_rect = player_surf.get_rect(midbottom=(80,ground))# pygame.Rect(left,top,width,height)

    player_gravity = 0

    

active_jump = 2
def jump():
    global active_jump, player_gravity
    if active_jump > 0:
       player_gravity = -10
       active_jump -= 1
    

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

game_start = True
game_play = False
game_pause = False
game_over = False

def check_game_status():
    global game_start, game_play, game_pause, game_over, pause_time_list
    print("game_start : ", game_start)
    print("game_play : ", game_play)
    print("game_pause : ", game_pause)
    print("game_over : ", game_over)
    print(pause_time_list)
    return   
           
# load static image
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
player_stand_surface = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand_rectangle = player_stand_surface.get_rect(center=(400,200))# pygame.Rect(left,top,width,height)
player_rotozoom = pygame.transform.rotozoom(player_stand_surface,0,2) #rotozoom(Obj, deg, x zoom)
player_rotozoom_rect= player_rotozoom.get_rect(center=(400,200))

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
    global player_gravity, game_pause, game_play, game_start,game_over, reset_time, pause_time, resume_time
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
            resume_time = pygame.time.get_ticks()
            if pause_time>0:
                pause_time_list.append(resume_time - pause_time)
        elif game_play: 
            game_pause = True
            game_play = False
            pause_time = pygame.time.get_ticks()
            
    elif i == 8:
        print("Hai premuto il pulsante ANALOGICO SX del controller")
        
    elif i == 9:
        print("Hai premuto il pulsante ANALOGICO DX del controller")
    elif i == 10: # don't work because I've Xbox, and open it
        print("Hai premuto il pulsante Home del controller")

    

# Start an infinite loop that will keep the game running until the user closes the window
while True:

    #### ALL EVENTS ####
    for event in pygame.event.get(): # Check for any events in the event queue
        if event.type == pygame.QUIT: # If the user closes the window
            pygame.quit() # Close Pygame and exit the program
            exit()  # Exit the program

        ### CONTROLLER BUTTON LINK ### because start and other bug don't work
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
        ### GAME_PLAY EVENTS ###
        if game_play: 
            if event.type == obstacle_timer:
                if randint(0,2): # generate 0, 1, 2; if 0 = False else >0 = True
                    obstacle_rect_list.append(snail[0].get_rect(bottomright= (randint(900,1100), ground)))
                else:
                    obstacle_rect_list.append(fly[0].get_rect(bottomright= (randint(900,1100), 150)))
        #    if event.type == pygame.MOUSEBUTTONDOWN:
        #        if player_walk_rectangle_1.collidepoint(event.pos): 
        #            player_gravity = -10 
        #     
        #    if event.type == pygame.MOUSEMOTION:
        #        if player_walk_rectangle_1.collidepoint(event.pos): 
        #            print('collision') 
        #    
        #    if event.type == pygame.KEYDOWN:
        #        if event.key == pygame.K_SPACE:
        #            game_play = False
        #            game_pause = True    
            
        # ### GAME_PAUSE EVENTS ###
        # elif game_pause:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             game_play = True
        #             game_pause = False
        #         if event.key == pygame.K_RETURN:
        #             print("invio")
        # ### GAME_START EVENTS ###
        # elif game_start: 
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RETURN:
        #             print("invio")
        #             reset_time = pygame.time.get_ticks()
        #             if game_start:
        #                 game_start = False
        #                 game_play = True
        # ### GAME_OVER EVENTS ###          
        # elif game_over: 
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RETURN:
        #             print("invio")
        #             reset_time = pygame.time.get_ticks()
        #             game_start = True
        #             game_over = False                

    #### GAME_START ####                 
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

    #### GAME_PLAY ####  
    if game_play:
        ### draw image background ###
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,sky_surface.get_height()))
        ### score ###
        display_score()
        pygame.draw.rect(screen, '#c0e8ec', score_rectangle.inflate(20, 10), 100)  # outer rectangle
        screen.blit(score_surface,score_rectangle)


        ### Obstacle ###
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        


        ### Player ###
        
        ## Moviment X : left_stick_x ##
        if pygame.time.get_ticks() >= move_timer: # Refresh character position based on fixed time interval
            player_rect.x += move_direction * player_speed * move_interval / 1000
            move_timer = pygame.time.get_ticks() + move_interval

        ## Moviment Y : Gravity and Jump ##
        player_gravity += 0.5
        player_rect.y += player_gravity
        if player_rect.bottom >= ground: 
            player_rect.bottom = ground 
            active_jump = 2  
        player_animation()
        screen.blit(player_surf, player_rect)

        ## Collision event ##
        for obstacle_rect in obstacle_rect_list:    
            if player_rect.colliderect(obstacle_rect): 
                game_over = True
                game_play = False
            
    #### GAME_OVER #### 
    elif game_over:
        game_over_surface = test_font.render('Game Over', False, 'Black') #render(text, AA, color)
        game_over_rectangle = game_over_surface.get_rect(midtop=(screen.get_width() / 2, 50))
        pygame.draw.rect(screen, 'Red', game_over_rectangle.inflate(20, 10), 100)  # outer rectangle
        screen.blit(game_over_surface,game_over_rectangle)

        restart_surface = test_font.render('Restart', False, 'Gold') #render(text, AA, color)
        restart_rectangle = restart_surface.get_rect(midtop=(screen.get_width() / 2, 250))
        pygame.draw.rect(screen, 'Red', restart_rectangle.inflate(50, 40), 100)  # outer rectangle
        screen.blit(restart_surface,restart_rectangle)
    #### GAME_PAUSE ####       
    elif game_pause:
        pause_message = test_font.render('Pause', False, 'Black') #render(text, AA, color)
        pause_rectangle = pause_message.get_rect(midtop=(screen.get_width() / 2, 200))
        pygame.draw.rect(screen, 'Gold', pause_rectangle.inflate(50, 30), 100)  # outer rectangle
        screen.blit(pause_message,pause_rectangle)


    # Update the game's graphics and display them on the screen
    pygame.display.update()
    clock.tick(60)


