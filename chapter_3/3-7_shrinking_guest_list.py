#eliminating guests

names = ["Jean", "Luchy", "Fernando", "Enma"]

for name in range(1, len(names)):
    if len(names) > 2:
        eli = names.pop()
        print(f"{eli}, sorry I cant invite you to dinner")
    else:
        continue

for name in names:
    print(f"{name}, your are invite to my dinner")
del names[0]
del names[0]





print(names)

