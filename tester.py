from simulator import *

def testAdd():
    print("Testing add()...", end="")
    assert(add(0, 0) == 0)
    assert(add(1, 2) == 3)
    assert(add(-1, -2) == -3)
    assert(add(-1, 2) == 1)
    print("passed!")

def testMultiply():
    print("Testing multiply()...", end="")
    assert(multiply(0, 0) == 0)
    assert(multiply(0, 1) == 0)
    assert(multiply(0, -1) == 0)
    assert(multiply(1, 1) == 1)
    assert(multiply(1, -1) == -1)
    assert(multiply(-1, -1) == 1)
    assert(multiply(2, 4) == 8)
    assert(multiply(2, -4) == -8)
    assert(multiply(-2, 4) == -8)
    assert(multiply(-2, -4) == 8)
    print("passed!")

def testDivide():
    print("Testing divide()...", end="")
    assert(divide(0, 1) == 0)
    assert(divide(0, -1) == 0)
    assert(divide(1, 1) == 1)
    assert(divide(1, -1) == -1)
    assert(divide(-1, -1) == 1)
    assert(divide(2, 4) == 1/2)
    assert(divide(2, -4) == -1/2)
    assert(divide(-2, 4) == -1/2)
    assert(divide(-2, -4) == 1/2)
    assert(divide(4, 2) == 2)
    assert(divide(-4, 2) == -2)
    assert(divide(4, -2) == -2)
    assert(divide(-4, -2) == 2)
    print("passed!")

def testSquare():
    print("Testing square()...", end="")
    assert(square(0) == 0)
    assert(square(1) == 1)
    assert(square(-1) == 1)
    assert(square(--1) == 1)
    assert(square(2) == 4)
    assert(square(2/4) == 1/4)
    assert(square(4) == 16)
    assert(square(-4) == 16)
    assert(square(4/2) == 4)
    assert(square(4/2) == square(2))
    print("passed!")

def testMod():
    print("Testing mod()...", end="")
    assert(mod(0, 1) == 0)
    assert(mod(0, -1) == 0)
    assert(mod(1, 1) == 0)
    assert(mod(1, -1) == 0)
    assert(mod(-1, -1) == 0)
    assert(mod(2, 4) == 2)
    assert(mod(2, -4) == -2)
    assert(mod(-2, 4) == 2)
    print("passed!")

def testDistance():
    print("Testing distance()...", end="")
    assert(distance(0, 0, 1, 0) == 1)
    assert(distance(0, 0, -1, 0) == 1)
    assert(distance(3, 1, 0, 4) == 5)
    print("passed!")

def testAll():
    print("Testing all simulator functions...")
    testAdd()
    testMultiply()
    testDivide()
    testSquare()
    testMod()
    testDistance()
    print("All simulator functions passed!")
    return True

testAll()
