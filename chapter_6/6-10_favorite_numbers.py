# Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_number = {
                    "Jean": [27,36],
                    "Luchy": [40,58],
                    "Enma": [60,21],
                    "Fernando": [15,37],
                    }

for key, values in favorite_number.items():
    print(f"{key} favorite number are: ")
    for value in values:
        print(f"{value}")
    print("\n")
