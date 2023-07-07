#exercise 10-2: learning c
#in learning_python.txt - replace Python with C#

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

transform = contents.replace('Python', 'C#')
print(transform)