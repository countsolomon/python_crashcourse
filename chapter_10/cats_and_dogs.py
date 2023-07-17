#exercise 10-8: cats and dogs
from pathlib import Path

c_path = Path('cats.txt')
d_path = Path('dogs.txt')


def print_it(contents):
    """print the contents to the screen"""
    lines = contents.splitlines()
    for line in lines:
        print(line)

try:
    c_contents = c_path.read_text()
    print_it(c_contents)
    d_contents = d_path.read_text()
except FileNotFoundError:
    pass
else: 
    print_it(d_contents)