#9-14 lottery 

from random import choice

#list provided. 10 numbers, and 5 letters. 
list = ['a', 'b', 6, 'Q', 'g', 58, 'o', 1, 2, 3, 65, 'x', 44, 45, 46, 47, 'a']

#first winner is selected from the list. 
first_number = choice(list)
second_number = choice(list)
third_number = choice(list)
fourth_number = choice(list)

winner_one = f"{first_number}, {second_number}, {third_number}, {fourth_number}"
print(winner_one)

