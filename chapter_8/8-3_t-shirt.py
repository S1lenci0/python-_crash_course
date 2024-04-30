# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"The size of the T-shirt is: {size}")
    print(f"The message of the t-shirt is: ")
    print(message.title())

size = input("Enter the size of the T-shirt: ")
message = input("Enter the message for the T-shirt: ")

make_shirt(size, message)
make_shirt(size="30", message="Hola mundo")
