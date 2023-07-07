#exercise 10-3: simple code 

from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)