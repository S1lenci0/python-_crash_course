# Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.


person_1 = {
                        "first_name": "Jean",
                        "last_name": "Marmolejos",
                        "age": 41,
                        "city": "Santiago"
                    }

person_2= {
                        "first_name": "Luchy",
                        "last_name": "Papapterra",
                        "age": 56,
                        "city": "Santiago"
                    }

person_3 = {
                        "first_name": "Enma",
                        "last_name": "Pappaterra",
                        "age": 41,
                        "city": "Punta Cana"
                    }

people = [person_1, person_2, person_3]
for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
    print("\n")

# for key,value in person_information.items():
#     print(f"{key} : {value}")