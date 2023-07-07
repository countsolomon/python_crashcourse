#exercise 10 - 1: learning python
#import and print out the text file in this directory
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

#loop through the contents
lines = contents.splitlines()
for line in lines: 
   print(line)
   
print('\n')

#store strings in a list and loop through the list
strings = [line for line in lines]
for string in strings:
    print(string)

