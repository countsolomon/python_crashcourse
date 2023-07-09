#exercise 10 - 4: guest book
from pathlib import Path

path = Path('guest_book.txt')

prompt = f"Welcome to the guest list."
prompt += f"When you are finished type 'End'"
prompt1 = f"Type in your name: "

print(prompt)
guest = input(prompt1)

# the list that will collect all the guest names.
guest_list = []

while guest != 'End':
    guest_list.append(guest)
    
#print out the list when finished 
for g in guest_list:
    print(g)

path.write_text(guest_list)
