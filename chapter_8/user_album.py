#8-8 make album function. 
#while loop inserted

def make_album(artist, album):
    """a function that creates an album for an muscian"""
    f_album = {'musician' : artist.title(), 'album_name' : album.title()}
    return f_album

prompt = f"\nHello, please enter an artist and album. "
prompt += f"\n(Type 'q' at any time. )"
while True: 
    print(prompt)
    artist_name = input("Artist name: ")
    if artist_name == 'q' or 'Q':
        break

    album_name = input("Album Name: ")
    if album_name == 'q' or 'Q':
        break

completed_album = make_album(artist_name, album_name)
print(completed_album)