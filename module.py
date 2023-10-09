from IPython.display import clear_output
import math

def printName(name):
    return f"Hello Mr/Ms {name}...we've been waiting for you!"

def circumference(radius):
    return (2 * math.pi * radius)
        
def square_footage(length, width):
    width = float(length)
    length = float(width)
    return length * width
    
    