# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

dream_vacation = {}
print("Write 'quit' to quit program")

while True:
    person = input("What is your name: ")
    if person == 'quit':
        break
    place = input("Tell the place of you Dream vacation: ")
    if place == 'quit':
        break
    dream_vacation[person] = place
    stop = input("Would you like to continue, yes/no: ")

    if stop == "y":
        continue
    elif stop == "n":
        break

for person, place in dream_vacation.items():
     print(f"{person} dream vacation place is {place}\n")

