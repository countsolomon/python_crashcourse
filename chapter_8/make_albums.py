#exercise 8-8
#artist , album , #t optional # of songs
#while loop that asks user albums. 
#provide quit value. 


#make_album function. 
def make_album(artist, album):
    """a function that creates an album for a muscian"""
    f_album = {'muscian' : artist.title(), 'album_name' : album.title()}
    return f_album

prompt = "\nEnter in an artist, and an album. "
prompt += "\n(When you are finished type 'q' for quit) "

while True:
    print(prompt)
    
    art_name = input("Artist name: ")
    if art_name == "q":
        break

    album_name = input("Album name: ")
    if album_name == "q":
        break

finish_album = make_album(art_name, album_name)
print(f"Hello, the music album you requested is: {finish_album}")