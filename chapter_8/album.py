#exercise 8-7 
#artist , album , #t optional # of songs

def make_album(artist, album, num_of_songs=None):
    """a function that creates an album for an muscian"""
    f_album = {'muscian' : artist.title(), 'album_name' : album.title()}
    if num_of_songs:
        f_album['number of songs'] = num_of_songs
    return f_album

three_imaginary_boys = make_album('the cure', 'three imaginary boys')
print(three_imaginary_boys)

riot = make_album('paramore', 'riot', num_of_songs='10')
print(riot)