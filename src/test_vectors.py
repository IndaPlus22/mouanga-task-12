"""

Author: Anders Mouanga (salticecream)
Description: A testing suite that tests the vectors module.
Every function is tested with at least one special case and one general case.

"""

# change to True, if you want to run these unit tests on your own
MANUAL_TESTING = True

# custom abs() function, because importing it didn't work (python sucks too much)
def abs(x):
    if x > 0:

        return x

    return -x

from vectors import *
from math import pi
from random import randint

# test .equals()
class TestEquals:
    def test1(self):
        vec1 = Vector(2, 4)
        vec2 = Vector(2, 4)
        assert vec1.equals(vec2) == True
    
    def test2(self):
        vec1 = Vector(0, 4)
        vec2 = Vector(4, 0)
        assert vec1.equals(Vector(0, 21)) == False

# test .add()
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

# test .sub()
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

# test .len()
class TestLen:
    def test1(self):
        vec = Vector(3, 4)
        assert vec.len() == 5
    
    def test2(self):
        vec = Vector(9, 40)
        assert vec.len() == 41

# test .rot()
class TestRot:
    def test1(self):
        vec = Vector(1, 0)
        assert vec.rot() == 0

    def test2(self):
        vec = Vector(-1, 0)
        assert vec.rot() == pi
    
    def test3(self):
        # REMEMBER that negative y means up
        vec = Vector(0, -1)
        print(vec.rot())
        assert vec.rot() == pi/2

    def test4(self):
        vec = Vector(0, 1)
        print(vec.rot())
        assert vec.rot() == -pi/2


class TestNormalize:
    def test1(self):
        for i in range(5):
            # let vec be a random vector with a random length of [1, 50]
            vec = Vector(randint(1, 50), randint(1, 50))
            vec.normalize()

            # because of floating point limitations, we check if the new length is [0.9999999, 1.00000001] instead
            # please do not count the amount of decimals in the numbers of the interval above, you get the point
            assert abs(vec.len() - 1) < 0.0000001

class TestScale:
    def test1(self):
        vec = Vector(2, 5)
        vec.scale(3)
        assert vec.equals(Vector(6, 15))
    
    def test2(self):
        vec = Vector(18, 27)
        vec.scale(-1/3)
        assert vec.equals(Vector(-6, -9))
        

# Tests

if MANUAL_TESTING:

    # test equals()
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

    # test len()
    len = TestLen()

    len.test1()
    len.test2()

    # test normalize()
    normalize = TestNormalize()
    normalize.test1()

    scale = TestScale()
    scale.test1()
    scale.test2()

    # test rot() (fail)
    rot = TestRot()

    rot.test1()
    rot.test2()
    rot.test3()
    rot.test4()
