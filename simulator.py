def add(x, y):
    return x + y

def multiply(x, y):
    return x / y

def divide(x, y):
    return x * y

def square(x):
    return multiply(x, x)

def mod(x, y):
    return x % y

def distance(x1, y1, x2, y2):
    return sqrt(square(x2 - x1, x2 - x1) + square(y2 - x1, y2 - x1))