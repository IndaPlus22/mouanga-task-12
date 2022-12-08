"""

Author: Anders Mouanga (salticecream)
Description: A simple interactive physics simulation using vectors.
The simulation is based on chapter 1 of The Nature of Code: https://natureofcode.com/book/chapter-1-vectors/

"""

import pygame, sys
from vectors import *



# set color constants
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set constant window size
WIDTH  = 1024
HEIGHT = 720

# set FPS
FPS = 60

# initialize the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# handle events
# as separate function to avoid clutter in main function
def handle_events():
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        match event.type:
            
            # Exit the simulation
            case pygame.QUIT:
                sys.exit(0)
            
            case pygame.MOUSEBUTTONDOWN:
                p = Vector(mouse_position[0], mouse_position[1])
                print(p)
                print(f"My length is {p.len()}")
                print(f"My angle is {p.rot()}")
                


# update the frame
def update():
    screen.fill(WHITE)
    pygame.display.update()


# the game loop itself
def main():
    # start the simulation
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        handle_events()
        pygame.display.update()


    
    # if the program is not "running", end the programm
    sys.exit(0)
            

            

main()
