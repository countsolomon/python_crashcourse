#exercise 10 - 4: guest book
from pathlib import Path

prompt = f"Welcome to the guest list."
prompt += f"\nType in your name."
prompt += f"\nWhen you are finished, type 'quit'. "

guest_book = []

while True:
    guest = input(prompt)

    if guest == 'quit':
        break
    else: 
        guest_book.append(guest)
    
written_guest_book = ''

for g in guest_book:
    written_guest_book = f"{written_guest_book} \n {g.title()}"

path = Path('guest_book.txt')
path.write_text(written_guest_book)
