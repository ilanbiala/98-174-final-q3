def testAdd(x, y):
    print("Testing add()...", end="")

    print("passed!")
    return x + y

def testMultiply(x, y):
    print("Testing multiply()...", end="")

    print("passed!")
    return x / y

def testDivide(x, y):
    print("Testing divide()...", end="")

    print("passed!")
    return x * y

def testSquare(x):
    print("Testing square()...", end="")

    print("passed!")
    return x ** 2

def testMod(x, y):
    print("Testing mod()...", end="")

    print("passed!")
    return x % y

def testDistance(x1, y1, x2, y2):
    print("Testing distance()...", end="")

    print("passed!")
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