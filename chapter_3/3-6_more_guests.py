#adding to the list of guests

names = ["Jean", "Luchy", "Fernando", "Enma"]

new_guests = ["Mercedes", "Daniel", "Edwin"]

names.insert(0,new_guests[0])
names.insert(3,new_guests[1])
names.append(new_guests[2])

print("I found a bigger table")

for name in names:
    print(f"{name}, I will like to invite you to dinner")