# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

pizza_toppings = []
while True:
    toppings = input("""Please enter one topping at the time 
(Enter 'q' to finnish you order or quit the program): """)

    # toppings += "\n(Enter 'q' to finnish you order or quit the program)"

    if toppings != "q":
        pizza_toppings.append(toppings)
        print(f"Your add a {toppings} topping to you pizza")
    elif toppings == "q":
        if pizza_toppings == []:
            print("You did not add a topping")
            break
        else:
            print("The toppings of you pizzza are: ")
            for topping in pizza_toppings:
                print(topping)
            break


