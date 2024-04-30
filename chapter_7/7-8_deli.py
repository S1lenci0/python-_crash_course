# Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I made
# your tuna sandwich. As each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.

sandwichs_orders =["tuna", "ham", "meat", "vegan"]
finished_sandwiches = []

while sandwichs_orders:
    current_sandwich = sandwichs_orders.pop()
    print(f"I made you {current_sandwich}")
    finished_sandwiches.append(current_sandwich)


print("I made this sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)