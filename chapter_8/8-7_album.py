# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a
# dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
# Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, number=None):
    artist_info = {"name": artist_name, "album": album_title}
    if number:
        artist_info["Number"] = number
    return artist_info

while True:
    print("Enter 'q' any time to finish the program")
    artist_name = input("Enter Artist name: ")
    if artist_name == "q":
        break

    album_title = input("Enter Artist Album: ")
    if album_title == "q":
        break

    number = input("Enter number of songs: ")
    if number == "q":
        break

    album = make_album(artist_name, album_title, number)
    for key, value in album.items():
        print(key, value)

#create at album dictionary for every artist info