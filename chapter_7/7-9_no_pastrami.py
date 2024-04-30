# Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwichs_orders =["tuna", "pastrani", "ham", "pastrani", "meat", "vegan", "pastrani"]
finished_sandwiches = []
print("The deli has run out of pastrani")
while sandwichs_orders:

    current_sandwich = sandwichs_orders.pop()
    if current_sandwich == "pastrani":
        continue
    print(f"I made you {current_sandwich}")
    finished_sandwiches.append(current_sandwich)


print("I made this sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)