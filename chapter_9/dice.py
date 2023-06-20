#exercise 9-13: dice
#the dice class

#import the module random, and the function random integer
from random import randint as RI

class Die:
    """The class that portrays a 6 sided die."""

    def __init__(self, sides=6):
        """Initialize the die class."""
        self.sides = sides

    
    def roll_die(self):
        """return a number between 1 and the sides of die"""
        return RI(1, self.sides)


#simulate rolling a 6-sided die
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die: ")
print(results)

#simulate rolling a 10-sided die
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die: ")
print(results)

#simulate rolling a 20-sided die
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die: ")
print(results)