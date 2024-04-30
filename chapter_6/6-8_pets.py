# Make several dictionaries, where each dictionary represents a different
# pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_1 = {
    "kind": "dog",
    "owner": "jean",
}

pet_2 = {
    "kind": "cat",
    "owner": "luchy",
}

pet_3 = {
    "kind": "lizar",
    "owner": "ferando",
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print("\n")