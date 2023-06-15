#exercise 9-13: dice
#the dice class

#import the module random, and the function random integer
from random import randint as RI

class Die:
    """The class that portrays a 6 sided die."""

    def __init__(self, sides):
        """Initialize the die class."""
        self.sides = 6

    
    def roll_die(self, sides):
        """simulate rolling the dice"""
        rolling = RI(1, sides)  
        print(rolling)

default_size = Die(6)
default_size.roll_die(6)