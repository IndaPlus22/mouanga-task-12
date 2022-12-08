"""

Author: Anders Mouanga (salticecream)
Description: A module that defines the sign(x) function as well as the Vector class.

"""

from math import atan, sqrt, pi

# get sign of a number
def sign(x):
    if x < 0:
        return -1

    elif x == 0:
        return 0

    return -1

class Vector:

    # constructor code
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # what to display when printed
    def __str__(self):
        return f"Vector ({self.x}, {self.y})"


    # get length of vector
    def len(self):
        return sqrt(self.x*self.x + self.y*self.y)

    # get angle, in radians, of a vector
    # where 0 is to the right and positive angles are measured counterclockwise relative to the x axis
    def rot(self):
        # i think this is how it works right?
        if self.x == 0:
            # we put the negative sign because in pygame, negative y means up
            return pi/2 * -sign(self.y)

        return atan(-self.y/self.x)
    
    # normalize the vector to length 1
    def normalize(self):
        if self.len() != 0:
            self.x /= self.len()
            self.y /= self.len()
    
    # add a vector to this vector
    def add(self, vec):
        self.x += vec.x
        self.y += vec.y
    
    # subtract a vector from this vector
    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    # multiply this vector with a scalar
    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

    