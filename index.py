import pygame # Import the Pygame module
from sys import exit # Import the "exit" function from the "sys" module

pygame.init() # Initialize the Pygame modules

# Create a game window with width 900 and height 500 and store it in a variable called "screen"
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('RunnerJump') # set 
#programIcon = pygame.image.load('icon.png')
#pygame.display.set_icon(programIcon)

# Create a Pygame clock object that will be used to regulate the game's frame rate
clock = pygame.time.Clock()
w = 100
h = 200
test_surface = pygame.Surface((w,h))
test_surface.fill('red')
# Start an infinite loop that will keep the game running until the user closes the window
while True:
    for event in pygame.event.get(): # Check for any events in the event queue
        if event.type == pygame.QUIT: # If the user closes the window
            pygame.quit() # Close Pygame and exit the program
            exit()  # Exit the program
    screen.blit(test_surface,(10,10))

    # Update the game's graphics and display them on the screen
    pygame.display.update()
    clock.tick(60)