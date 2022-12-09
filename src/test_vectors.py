"""

Author: Anders Mouanga (salticecream)
Description: A testing suite that tests the vectors module.

"""
from time import sleep

# change to True, if you want to run these unit tests on your own
# in that case you simply need to run this file

MANUAL_TESTING = False

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
        assert vec.rot() == pi/2

    def test4(self):
        vec = Vector(0, 1)
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

    # test scale()
    scale = TestScale()
    scale.test1()
    scale.test2()

    # test rot() (fail)
    rot = TestRot()
    rot.test1()
    rot.test2()
    rot.test3()
    rot.test4()

    print("""all tests passed. obviously. of course they did. what, did you expect non-working code from me?
are you serious? me, anders mouanga????? writing some kind of SOFTWARE BUG????? 
this is the best piece of software you'll ever see in your life. 
i don't even need tests, i just did this for fun because i knew they would all pass. 
the computer itself fears me, the COMPILER ITSELF. FEARS. ME. 
i could write "assert False" and still not crash. 
i can make code inside of a "while False" loop run. 
i am the inventor of the first O(log n) sorting algorithm. 
i once forced the computer to divide by zero for me. then i noticed it was getting a little slow so i started doing all of the CPU arithmetic in my head instead.
in this way i simulated multi-molecular quantum physics in the time it takes for your useless little machine to perform a clock cycle. 
anyway, you're gonna read this text if you doubt me for some reason and run the tests yourself instead of letting pytest do it for you. and you're gonna realize i'm damn right.""")
    sleep(10)