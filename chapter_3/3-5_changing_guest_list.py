#changing the list
names = ["Jean", "Luchy", "Fernando", "Enma"]

cancel = ["Jean", "Enma"]

for name in names:
    if name in cancel:
        names.remove(name)

for name in names:
    print(f"{name}, I will like you to invite you to dinner")






#print("Jean", "Enma")