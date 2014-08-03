__author__ = 'Alfred'

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def apply(func, x, y):
    return func(x, y)

apply(add, 2, 1)

apply(sub, 2, 1)
