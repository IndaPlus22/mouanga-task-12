"""

Author: Anders Mouanga (salticecream)
Description: A testing suite that tests the vectors module.
Every function is tested with at least one special case and one general case.

"""

# change to True, if you want to run these unit tests on your own
MANUAL_TESTING = True

from vectors import *
from random import randint

class TestEquals:
    def test1(self):
        vec1 = Vector(2, 4)
        vec2 = Vector(2, 4)
        assert vec1.equals(vec2) == True
    
    def test2(self):
        vec1 = Vector(0, 4)
        vec2 = Vector(4, 0)
        assert vec1.equals(Vector(0, 21)) == False

class TestAdd:
    def test1(self):
        vec1 = Vector(3, 4)
        vec2 = Vector(5, 5)
        vec1.add(vec2)
        assert vec1.equals(Vector(8, 9))
    
    def test2(self):
        vec1 = Vector(0, 4)
        vec2 = Vector(0, -17)
        vec1.add(vec2)
        assert vec1.equals(Vector(0, -13))

class TestSub:
    def test1(self):
        vec1 = Vector(3, 4)
        vec2 = Vector(5, 5)
        vec1.sub(vec2)
        assert vec1.equals(Vector(-2, -1))
    
    def test2(self):
        vec1 = Vector(0, 4)
        vec2 = Vector(0, -17)
        vec1.sub(vec2)
        assert vec1.equals(Vector(0, 21))


# Tests

if MANUAL_TESTING:
    equals = TestEquals()

    equals.test1()
    equals.test2()

    # test add()
    add = TestAdd()

    add.test1()
    add.test2()

    # test sub()
    sub = TestSub()

    sub.test1()
    sub.test2()