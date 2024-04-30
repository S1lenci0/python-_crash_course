# Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number
# of arguments each time.
lista = []
def make_sandwiches(*args):
    """function that take the ingridients of
    your sandwiches"""

    print("Write what do you want in you sandwich one ingridient at the time")
    print("type 'q' when you are finish")

    while True:

        args = input("Enter your ingredient here: ")
        lista.append(args)


        if args == "q":
            lista.pop()
            return lista
            break


def print_ingredients(make_sandwiches):
    if make_sandwiches == None:
        print("Your list is empty")
    for item in make_sandwiches:
        print(item)

make_sandwiches()
print_ingredients(make_sandwiches())
print(lista)
#create a function that take the arguments and
# put it in a tuple them create a function that take that tuple and print
#the information to the user