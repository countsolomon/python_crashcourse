#using json file: add username, department, and fav color
from pathlib import Path
import json

def get_stored_username(path):
    """Get the stored username."""
    if path.exists():
       contents = path.read_text()    
       user_dict = json.loads(contents)
       return user_dict
    else:
        return None

def get_new_user_dict(path):
    """Make a new user dictionary."""
    user_name = input("What is your name? ")
    user_depart = input("What department are you in? ")
    user_color = input("What is your favorite color? ")
    user_dict = {"username": user_name, 
                 "department": user_depart, 
                 "favorite color": user_color
                 }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict
       
def greet_user():
    """Greet the user by name"""
    path = Path('user_dict.json')
    user_dict = get_stored_username(path)
    if user_dict:
        print(f'Welcome back, {user_dict["username"]}!')
        print(f'The department you are in is: {user_dict["department"]}.')
        print(f'Your favorite color is: {user_dict["favorite color"]}')
    else:
        user_dict = get_new_user_dict(path)
        print(f'We will remember you when you come back, {user_dict["username"]}!')
        
greet_user()
get_stored_username('user_dict.json')