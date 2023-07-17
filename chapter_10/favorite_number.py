#user inputs their fav number and stores as JSON. 
from pathlib import Path
import json

#make a json file with the favorite number. 
path = Path('fav_num.json')
fav_num = input('What is your favorite number? ')
contents = json.dumps(fav_num)
path.write_text(contents)

#read fav_num.json into the program

contents = path.read_text()
fav_num = json.loads(contents)
print(f"Your favorite number is {fav_num}.")