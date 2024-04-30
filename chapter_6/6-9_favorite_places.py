# Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places for
# each person. To make this exercise a bit more interesting, ask some friends to
# name a few of their favorite places. Loop through the dictionary, and print each
# person’s name and their favorite places

favorte_places = {
    "fernado": ["NYC","miami", "roma"],
    "enma": ["punta cana", "santo domingo", "samana"],
    "luchy": ["santiago", "santo domingo", "puerto plata"]
}

for name, places in favorte_places.items():
    print(f"{name.title()} favorite places are: ")
    for place in places:
        print(f"{place.title()}")
    print("\n")