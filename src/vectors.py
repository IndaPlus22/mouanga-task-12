"""

Author: Anders Mouanga (salticecream)
Description: A module that defines the Vector class.

"""

from math import acos, sqrt, pi
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

        if self.len() == 0:
            return 0 # and avoid the division by zero error

        if self.y > 0:
            return -acos(self.x / self.len())

        return acos(self.x / self.len())
    
    # normalize the vector to length 1
    def normalize(self):
        if self.len() != 0:
            # we store the starting length first, so it doesn't change between divisions
            len = self.len()
            self.x /= len
            self.y /= len
    
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
    
    # check if this vector is the same as another vector
    def equals(self, vec):
        if self.x == vec.x and self.y == vec.y:
            return True
        return False
     

    
