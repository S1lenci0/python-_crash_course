# Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

available_seets = input("How many are you people are in their dinner group: ")
if int(available_seets) > 8:
    print("Sorry you have to wait for a open table")
else:
    print("Your table is ready!")