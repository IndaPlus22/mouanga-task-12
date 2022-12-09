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
# additional comment: like none of these are used lmao
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (225, 30, 30)
BLUE = (30, 30, 225)
PURPLE = (127, 15, 127)

# set constant window size
WIDTH  = 1366
HEIGHT = 768

# set FPS
FPS = 144

# initialize the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# define the Ball class
class Ball:

    # constructor code
    def __init__ (self, pos: Vector, speed: Vector, acceleration: Vector):
        self.pos = pos
        self.speed = speed
        self.acceleration = acceleration
        self.color = BLACK

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
        if self.pos.x < -50:
            self.pos.x += (WIDTH + 100)
        # right
        if self.pos.x > WIDTH+50:
            self.pos.x -= (WIDTH + 100)
        # up
        if self.pos.y < -50:
            self.pos.y += (HEIGHT + 100)
        # down
        if self.pos.y > HEIGHT+50:
            self.pos.y -= (HEIGHT + 100)
    
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
        jerk.scale(0.1)
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

    # move the ball on keyboard input       
    if pygame.key.get_pressed()[pygame.K_1]:
        ball.attract()
        ball.color = BLUE
    elif pygame.key.get_pressed()[pygame.K_2]:
        ball.repel()
        ball.color = RED
    elif pygame.key.get_pressed()[pygame.K_3]:
        ball.random()
        ball.color = PURPLE
    else:
        ball.acceleration.scale(0.98)
        ball.speed.scale(0.98)
        ball.color = BLACK


# update the screen and the game
def update():
    mouse_position = pygame.mouse.get_pos()

    # draw background
    screen.fill(WHITE)

    # draw the ball
    ball.update()
    pygame.draw.circle(screen, ball.color, (ball.pos.x, ball.pos.y), 40, 0)
    
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
