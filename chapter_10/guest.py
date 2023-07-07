#exercise 10 - 4: Guest
#a program that prompts the user for their name. 
#program then writes the users name to a file. 
from pathlib import Path

prompt = 'What is your name? '
name = input(prompt)

path = Path('guest.txt')
path.write_text(name)