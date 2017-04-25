def testAdd(x, y):
    print("Testing add()...", end="")
    assert(add(0, 0) == 0)
    assert(add(1, 2) == 3)
    assert(add(-1, -2) == -3)
    assert(add(-1, 2) == 1)
    print("passed!")

def testMultiply(x, y):
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

def testDivide(x, y):
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

def testSquare(x):
    print("Testing square()...", end="")
    assert(square(0) == 0)
    assert(square(1) == 1)
    assert(square(-1) == -1)
    assert(square(--1) == 1)
    assert(square(2) == 4)
    assert(square(2/4) == 1/4)
    assert(square(4) == 16)
    assert(square(-4) == 16)
    assert(square(4/2) == 4)
    assert(square(4/2) == square(2))
    print("passed!")

def testMod(x, y):
    print("Testing mod()...", end="")
    raise Exception("Will be added later!")
    return x % y

def testDistance(x1, y1, x2, y2):
    print("Testing distance()...", end="")

    raise Exception("Will be added later!")
    return sqrt(square(x2 - x1, x2 - x1) + square(y2 - x1, y2 - x1))

def testAll():
    print("Testing all simulator functions...")
    testAdd()
    testMultiply()
    testDivide()
    testSquare()
    testMod()
    testDistance()
    print("All simulator functions passed!")
