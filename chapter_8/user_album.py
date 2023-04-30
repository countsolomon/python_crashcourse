#8-8 make album function. 
#while loop inserted

def make_album(artist, album, num_of_songs=None):
    """a function that creates an album for an muscian"""
    f_album = {'muscian' : artist.title(), 'album_name' : album.title()}
    if num_of_songs:
        f_album['number of songs'] = num_of_songs
    return f_album

prompt = f"\nHello, please enter an artist and album. "
prompt += f"\n(Type 'q' at any time. )"
while True: 
    print(prompt)
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_name = input("Album Name: ")
    if album_name == 'q':
        break

complete_album = 