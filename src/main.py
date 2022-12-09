"""

Author: Anders Mouanga (salticecream)
Description: A simple interactive physics simulation using vectors.
The simulation is based on chapter 1 of The Nature of Code: https://natureofcode.com/book/chapter-1-vectors/

CONTROLS:
1 - ATTRACT (accelerate ball towards your cursor)
2 - REPEL   (accelerate ball away from your cursor)
3 - RANDOM  (accelerate ball in random direction)

"""

import pygame, sys
from vectors import *
from random import randint
pygame.init()


# set color constants
# additional comment: none of these are used lmao
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
FPS = 144

# set font
FONT = pygame.font.Font(None, 25)

# initialize the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# define the Ball class
class Ball:

    # constructor code
    def __init__ (self, pos: Vector, speed: Vector, acceleration: Vector):
        self.pos = pos
        self.speed = speed
        self.acceleration = acceleration

    # we make the acceleration and speed actually do something
    def update(self):
        # add some drag to the ball
        self.acceleration.scale(0.96)
        self.speed.scale(0.98)

        # update the speed and acceleration
        self.speed.add(self.acceleration)
        self.pos.add(self.speed)

        # wrap around
        # left
        if self.pos.x < -20:
            self.pos.x += WIDTH
        # right
        if self.pos.x > WIDTH+20:
            self.pos.x -= WIDTH
        # up
        if self.pos.y < -20:
            self.pos.y += HEIGHT
        # down
        if self.pos.y > HEIGHT+20:
            self.pos.y -= HEIGHT
    
    # accelerate the ball towards the cursor
    def attract(self):

        # generate a list to store the mouse's relative position
        mouse_position = pygame.mouse.get_pos()
        mouse_relative_position = []
        mouse_relative_position.append(mouse_position[0])
        mouse_relative_position.append(mouse_position[1])
        mouse_relative_position[0] -= self.pos.x
        mouse_relative_position[1] -= self.pos.y

        # jerk is the derivative of acceleration wrt time
        jerk = Vector(mouse_relative_position[0], mouse_relative_position[1]) 
        jerk.normalize()
        jerk.scale(0.01)
        self.acceleration.add(jerk)

    # like attract() but with .sub()
    def repel(self):

        mouse_position = pygame.mouse.get_pos()
        mouse_relative_position = []
        mouse_relative_position.append(mouse_position[0])
        mouse_relative_position.append(mouse_position[1])
        mouse_relative_position[0] -= self.pos.x
        mouse_relative_position[1] -= self.pos.y

        # jerk is the derivative of acceleration wrt time
        jerk = Vector(mouse_relative_position[0], mouse_relative_position[1]) 
        jerk.normalize()
        jerk.scale(0.01)
        self.acceleration.sub(jerk)
    
    # accelerate the ball randomly
    def random(self):
        # jerk is the derivative of acceleration wrt time
        jerk = Vector(randint(-50, 50), randint(-50, 50)) 
        jerk.normalize()
        jerk.scale(0.01)
        self.acceleration.add(jerk)
    

# handle events
# as separate function to avoid clutter in main function
def handle_events():
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        match event.type:
            # i was planning on putting more events in here but then i didn't
            case pygame.QUIT:
                sys.exit(0)
            
    if pygame.key.get_pressed()[pygame.K_1]:
        ball.attract()
    elif pygame.key.get_pressed()[pygame.K_2]:
        ball.repel()
    elif pygame.key.get_pressed()[pygame.K_3]:
        ball.random()


# update the screen and the game
def update():
    mouse_position = pygame.mouse.get_pos()
    vector = Vector(mouse_position[0] - ball.pos.x, mouse_position[1] - ball.pos.y)
    text = FONT.render(
        f"({round(vector.x, 1)}, {round(vector.y, 1)}) | len: {round(vector.len(), 2)} | angle: {round(vector.rot(), 2)}",
        False,
        BLACK
    )
    # draw background
    screen.fill(WHITE)
    screen.blit(text, (mouse_position[0], mouse_position[1] - 20))

    # draw the ball
    ball.update()
    pygame.draw.circle(screen, BLACK, (ball.pos.x, ball.pos.y), 10, 0)

    # draw text
    
    pygame.display.flip()
    pygame.display.update()


# the game loop itself
def main():
    # start the simulation
    clock = pygame.time.Clock()
    global ball
    ball = Ball(
        Vector(WIDTH/2, HEIGHT/2),
        Vector(0, 0),
        Vector(0, 0)
    )
    running = True
    while running:
        clock.tick(FPS)
        handle_events()
        update()


    
    # after the program has finished "running", end the program
    sys.exit(0)

main()
